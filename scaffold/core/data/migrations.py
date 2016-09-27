import os
import sys
import argparse

try:
    import pymysql 
    pymysql.install_as_MySQLdb()
    import MySQLdb
except ImportError:
    import MySQLdb


sys.path.append(os.path.abspath('./'))

#import config from current folder if it exists
current_path_settings = os.getcwd() + os.sep + 'config/settings.py'
sys.path.append(current_path_settings)
if os.path.exists(current_path_settings):
    from config import settings

from scaffold.core.data.database import db as dataset
#from database import db as dataset
from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data


def text_num_split(value):
    return (
        ''.join([c for c in value if c.isalpha()]), 
        ''.join([c for c in value if c.isdigit()]))

class select_structure(select_data):
    required = {'TABLE_NAME'}
    count_rows = False
    limit_enabled = False
    query_str = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS"
    columns_where = ['TABLE_NAME']
    groups = ['TABLE_NAME']

    def __iter__(self):
        with dataset() as database:
            for row in database.fetchall(self.query(), values=self.data):
                yield row


class get_database_info(select_structure):
    required = {'TABLE_SCHEMA'}
    count_rows = False
    limit_enabled = False
    query_str = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS"
    columns_where = ['TABLE_SCHEMA']
    grouping = []
    
    def __iter__(self):
        with dataset() as database:
            for row in database.fetchall(self.query(), values=self.data):
                yield row

class get_tables(select_structure):
    required = {'TABLE_SCHEMA'}
    count_rows = False
    limit_enabled = False
    query_str = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS"
    columns_where = ['TABLE_SCHEMA']
    grouping = ['TABLE_NAME']
    
    def __iter__(self):
        with dataset() as database:
            print(self.query())
            for row in database.fetchall(self.query(), values=self.data):
                yield row

class get_table_columns(select_structure):
    debug = True
    required = {'TABLE_SCHEMA', 'TABLE_NAME'}
    count_rows = False
    limit_enabled = False
    query_str = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS"
    columns_where = ['TABLE_SCHEMA', 'TABLE_NAME']
    grouping = ['TABLE_NAME', 'COLUMN_NAME']

class get_table_column_indexes(select_structure):
    required = {'TABLE_SCHEMA', 'TABLE_NAME'}
    count_rows = False
    limit_enabled = False
    #~ query_str = "SELECT table_name, index_name, GROUP_CONCAT(column_name ORDER BY seq_in_index) as column_name FROM information_schema.statistics "
    query_str = "SELECT table_schema, table_name, index_name, column_name, NON_UNIQUE as unique_index FROM information_schema.statistics "
    columns_where = ['TABLE_SCHEMA', 'TABLE_NAME']
    #grouping = ['1', '2']

class create_tables(insert_data):
    required = {'table_name'}
    query_str = [u"CREATE TABLE IF NOT EXISTS %s (`id` int(10) unsigned NOT NULL AUTO_INCREMENT, PRIMARY KEY (`id`), UNIQUE KEY `id_UNIQUE` (`id`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;\n"]

    def execute(self, data):
        self.set(data)
        with dataset() as database:
            print(self.query() % self.data['table_name'])
            database.execute(
                self.query() % self.data['table_name'])

def export_schema(args, export_path='./data/migrate'):
    set_database_details(database=args)
    export_path = args.get('target', export_path)
    if dataset().connection_settings.get('type') is None:
        sys.exit('Unknown database type')
    if dataset().connection_settings.get('host') is None:
        sys.exit("Missing database config")
    if dataset().connection_settings.get('db'):
        schema_name = dataset().connection_settings.get('db')
    else:
        schema_name = dataset().connection_settings.get('host')
    print("Exporting %s" % schema_name)
    print(dataset().connection_settings)
    table_list = []
    with open('%s/generated_tables.sql' % export_path, 'w') as tab_fp:
        print('Migrating database named %s' % schema_name)
        tables = get_tables({'TABLE_SCHEMA': schema_name})
        for table in tables:
            print(table)
            tab_fp.write("CREATE TABLE IF NOT EXISTS %s;\n" % table['TABLE_NAME'])
            table_list.append(table['TABLE_NAME'])

    with open('%s/clean.sql' % export_path, 'w') as tab_fp:
        tab_fp.write("SET FOREIGN_KEY_CHECKS = 0;\n")
        for table in table_list:
            tab_fp.write("TRUNCATE %s;\n" % table)
            tab_fp.write("ALTER TABLE %s AUTO_INCREMENT = 1;;\n" % table)
        tab_fp.write("SET FOREIGN_KEY_CHECKS = 1;\n")

    with open(os.path.realpath('%s/generated_columns.sql' % export_path), 'w') as col_fp:
        col_fp.write('table_name, column_name, column_type, default\n')
        for table in table_list:
            columns = get_table_columns({'TABLE_SCHEMA': schema_name, 'TABLE_NAME': table})
            col_fp.write("#%s\n" % table)
            print(table)
            for column in columns:
                print("\t" + column['COLUMN_NAME'])
                #~ print column['COLUMN_KEY']
                #~ print column['NUMERIC_SCALE']
                #~ print column['EXTRA']
                column_type = column['DATA_TYPE']
                column_type, column_value = text_num_split(column['COLUMN_TYPE'].split(' ')[-1])

                data = {
                    'table': table,
                    'primary': ' PRIMARY KEY (`%s`) ' % column['COLUMN_NAME'] if 'pri' in column['COLUMN_KEY'].lower() else '',
                    'nullable': 'NULL ' if column['IS_NULLABLE'].lower() == 'yes' else '',
                    'increment': 'AUTO_INCREMENT ' if 'auto_increment' in column['EXTRA'].lower() else '',
                    'default': '' if column['COLUMN_DEFAULT'] is None else 'DEFAULT %s' % column['COLUMN_DEFAULT'],
                    'column': column['COLUMN_NAME'],
                    'column_type': column['COLUMN_TYPE'],
                    'comment': column['COLUMN_COMMENT']}

                #ALTER TABLE `tickets` ADD COLUMN `id` INT UNSIGNED NOT NULL AUTO_INCREMENT, ADD PRIMARY KEY (`id`), ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
                col_fp.write("ALTER TABLE {table} ADD COLUMN {column} {column_type} {nullable}{primary}{increment}{default};\n".format(**data))
                col_fp.write("ALTER TABLE {table} CHANGE COLUMN {column} {column} {column_type} {nullable}{primary}{increment}{default};\n".format(**data))

            col_fp.write("\n\n")


    with open('%s/generated_column_indexes.sql' % export_path, 'w') as col_fp:
        col_fp.write('table_name, column_name, column_type, default\n')
        for table in table_list:
            columns = get_table_column_indexes({'TABLE_SCHEMA': schema_name, 'TABLE_NAME': table})
            col_fp.write("#%s\n" % table)
            for column in columns:
                print(column)
                if column['index_name'] == 'PRIMARY':
                    continue
                if column['unique_index'] == 0:
                    col_fp.write("ALTER TABLE %s ADD INDEX %s (%s ASC);\n" % (table, column['index_name'], column['column_name']))
                else:
                    col_fp.write("ALTER TABLE %s ADD UNIQUE INDEX %s (%s ASC);\n" % (table, column['index_name'], column['column_name']))

            col_fp.write("\n\n")
        #columns = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = %s;" % schema_name


def set_database_details(database):
    #database = args
    if database:
        database['db'] = database['database']
        database['user'] = database['username']
        database['passwd'] = database['password']
        dataset.config(database)


def import_schema(args, import_path='./data/migrate'):
    set_database_details(database=args)
    print("Importing into %s" % dataset().connection_settings.get('db'))
    table_list = []
    columns = []
    column_indexes = []
    for filename in ['%s/generated_columns.sql' % import_path, '%s/generated_column_indexes.sql' % import_path]:
        with open(filename, 'r') as col_fp:
            for line in col_fp.readlines():
                if line.startswith('ALTER TABLE '):
                    sp = line.split()
                    table=None
                    if 'ADD INDEX ' in line:
                        table = line.partition(' ADD INDEX ')[0].lstrip('ALTER TABLE ')
                        column_indexes.append(line)
                    if 'ADD COLUMN ' in line:
                        table = line.partition(' ADD COLUMN ')[0].lstrip('ALTER TABLE ')
                    if 'CHANGE COLUMN ' in line:
                        table = line.partition(' CHANGE COLUMN ')[0].lstrip('ALTER TABLE ')
                    if table:
                        print(table)
                        #~ table, ignore, line = line.partition('ADD COLUMN ')
                        table_list.append(table.strip())
                        columns.append(line)
    
    table_list=set(table_list)
    insert_tables = create_tables()
    for table in set(table_list):
        print(table)
        try:
            insert_tables.execute({'table_name': table})
        except MySQLdb.Error as e:
            print(e)

    for column in columns:
        with dataset() as database:
            print(column)
            try:
                database.execute(column)
            except MySQLdb.Error as e:
                print(e)
                
    for column in column_indexes:
        with dataset() as database:
            print(column)
            try:
                database.execute(column)
            except MySQLdb.Error as e:
                print(e)
