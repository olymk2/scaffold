import os
import sys

try:
    import pymysql 
    pymysql.install_as_MySQLdb()
    import MySQLdb
except ImportError:
    import MySQLdb
import MySQLdb.cursors

import sqlite3
try:
    import psycopg2 as pgdb
except:
    pass
DBTYPE_MYSQL = 0 
DBTYPE_SQLLITE = 1
DBTYPE_POSTGRES = 1

class db:
    name = None
    connection = None
    connection_settings = {}
    dbtype = DBTYPE_MYSQL  # 0 = mysql, 1 = sqllite
    cursor = None
    debug = False

    @classmethod
    def config(cls, connection_settings):
        cls.connection_settings = connection_settings

    def __enter__(self):
        connection_details = db.connection_settings
        dbtype = db.connection_settings.get('type', 'mysql')

        if connection_details.get('location') is not None:
            connection_details['host'] = connection_details['location']
            del(connection_details['location'])

        self.use_commit = True

        #mysql database
        if dbtype == 'mysql':
            db.dbtype = DBTYPE_MYSQL
            self.connection = MySQLdb.connect(
                host = connection_details.get('host'),
                user = connection_details.get('user'),
                passwd = connection_details.get('passwd'),
                db = connection_details.get('db'),
                #charset = connection_details.get('charset', 'utf-8'),
                port = connection_details.get('port', 3306))
            self.connection.set_charset('utf8')
            self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
            return self

        #sqllite database
        if dbtype == 'sqllite':
            db.dbtype = DBTYPE_SQLLITE
            #self.use_commit = False
            self.connection = sqlite3.connect(connection_details['host'])
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            return self

        #postgres database
        if dbtype == 'pgsql':
            db.dbtype = DBTYPE_POSTGRES
            self.connection = pgdb.connect(**connection_details)
            self.cursor = self.connection.cursor(cursorclass=pgdb.extras.DictCursor)
        return self

    def commit(self):
        if self.use_commit is True:
            self.connection.commit()

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        self.commit()
        self.connection.close()

    def build_where(self, columns, params, query=''):
        """build where conditions dynamically insert the columns to test and invalidate missing params"""
        where_conditions = []
        for c in columns:
            current_column = c.split('.')[-1]
            if params.get(current_column, ''):
                where_conditions.append(c+ "=%(" + current_column + ")s")
            else:
                where_conditions.append(c + '=' + c)
        return query + ' where ' + ' AND '.join(where_conditions)

    def clean_field_names(self, values):
        fields = []
        for item in range(0, len(values)):
            if values[item].endswith('_id'):
                v = values[item][0:len(values[item]) - 3].replace('_', ' ')
            else:
                v = values[item].replace('_', ' ')
            fields.append(v)
        return fields

    def escape(self, value):
        if int == type(value) or long == type(value):
            value = str(value)
        return self.connection.escape_string(value)

    def columns(self, table):
        self.cursor.execute('show columns from ' + table)
        fieldnames = []
        for column in self.cursor.fetchall():
            if column['Field'] != 'id':
                fieldnames.append(column['Field'].strip())
        return fieldnames

    def fetchone(self, sql, values=None):
        if not values:
            values = []
        if self.debug:
            print(sql.format(values))
        self.execute_query(sql, values)
        return self.cursor.fetchone()

    def execute_query(self, sql, values):
        try:    
            self.cursor.execute(sql, values)
            self.commit()
        except MySQLdb.Error as e:
            print(e)
            print(sql)
            self.connection.rollback()              # rollback transaction here

    def fetchall(self, sql, values=None):
        if not values:
            values = []
        if self.debug:
            print(sql.format(values))
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def last_id(self):
        return self.cursor.lastrowid

    def execute(self, sql, values=None):
        if not values:
            values = []
        if self.debug:
            print(sql.format(values))
        self.execute_query(sql, values)
        # self.cursor.execute(sql, values)
        #return self.commit()

    def insert(self, table, fieldnames=(), values=()):
        value_placeholder = ''
        for v in values:
            value_placeholder += u'%s,'
        sql = u'insert into ' + table + u' (`' + u'`,`'.join(fieldnames) + u'`) VALUES (' + value_placeholder.rstrip(',') + u');'
        if self.debug:
            print(sql.format(values))
        result = self.cursor.execute(sql, values)
        #self.cursor.commit()
        return result

    def insert_paginated(self, table, fieldnames, rows=100):
        values = []
        item = yield
        while item:
            if len(values) == rows:
                self.mass_insert(table, fieldnames, values)
                item = yield
                values = [item]
            item = yield
            if item:
                values.append(item)
        self.mass_insert(table, fieldnames, values)

    def mass_insert(self, table, fieldnames, values):
        value_placeholder = ''
        for v in fieldnames:
            value_placeholder += u'%s,'
        sql = u'insert into ' + table + u' (`' + u'`,`'.join(fieldnames) + u'`) VALUES (' + value_placeholder.rstrip(',') + u')'
        if self.debug:
            print(sql.format(values))
        #passing parameters in this way auto escapes them and supports unicode better
        return self.cursor.executemany(sql, values)

    def insert_duplicate(self, table, fieldnames, values):
        escape_values = []
        for v in values:
            escape_values.append(self.connection.escape_string(str(v).strip('"')))

        update = ''
        for item in range(1, len(fieldnames)):
            value = values[item]
            if value is None:
                value = ''
            update += fieldnames[item] + '=' + self.connection.escape_string(unicode(value, encoding='UTF-8').strip('"'))

        sql = u'insert into ' + table + u' (`' + '`,`'.join(fieldnames) + u'`) VALUES (' + u'","'.join(escape_values) + u') ON DUPLICATE KEY UPDATE ' + update + u';'
        return self.cursor.execute(sql)

    def update(self, table, where=(), fieldnames=(), values=()):
        update = []
        for item in range(0, len(fieldnames)):
            value = values[item]
            if value is None:
                value = ''
            update.append('`' + fieldnames[item] + '`="' + self.connection.escape_string(str(value).strip('"')) + '"')
        sql = 'update ' + table + ' set ' + ', '.join(update) + ' where ' + ' and '.join(where) + ';'
        if self.debug:
            print(sql.format(values))
        return self.cursor.execute(sql)

    def exists(self, table, where):
        conditions = []
        field_list = []
        for field, value in where.items():
            field_list.append(value)
            conditions.append('`' + field + '`=%s')
        sql = 'select count(*) as `count` from `' + table + '` where ' + ' and '.join(conditions) + ';'
        self.cursor.execute(sql, field_list)
        total = self.cursor.fetchone()['count']
        return total
