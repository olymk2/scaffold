import os
import sys
from .database import DBTYPE_MYSQL, DBTYPE_SQLLITE
from .database import db as dataset
from .helper import required_values
from ..validate import validate

class query(object):
    debug = False
    query = ''
    query_str = None
    query_file = None
    query_offset = 0

    table = None

    # enforce that these exist required values
    required = set()
    #~ values_optional = {}
    
    
    #select insert or update columns enforce that these exist
    columns = {}

    #where columns enfore that these exist, default to id to avoid user mistakes
    columns_where = {'id'}
    
    #these are optional so we can exclude them
    columns_optional = {}
    
    validate_data = {}
    
    sql_where = None

    # if set this will override the generated sql
    sql = None 

    def __init__(self):
        self.query_offset = 0

    def __call__(self):
        self.query_offset = 0
        return self

    def calculated_data(self):
        return {}

    def set(self, data):
        """set the query data make sure we have all required values"""
        if data is None:
            return
        self.data = data
        #required_values(self.data, required=self.required)
        
        for key, value in self.calculated_data().items():
            self.data[key] = value
        

    def query(self):
        return self.sql

    def execute(self, data, sql):
        self.sql = sql
        with dataset() as database:
            database.execute(sql, data)

    def clean_data(self):
        # convert missing values to null automatically
        self.validator = validate()
        for key, value in self.data.items():
            if value is None:
                self.data[key] = None
                continue
            self.data[key] = value

class query_builder:
    query_path = os.path.abspath('./data/sql/')
    sql_where = None
    debug = False
    type = 0 #0 = mysql

    named_param_before = '%('
    named_param_after = ')s'

    # if we get a key constrint dont raise an error
    expect_duplicates = True

    ignore_clause = 'ignore '

    @classmethod
    def set_path(cls, path):
        cls.query_path = os.path.abspath(path)
        if os.path.exists(cls.query_path):
            return 
        print('Missing query folder %s' % cls.query_path)

    def set_where(self, where):
        self.sql_where = where
    
    def __init__(self, mode=0, table=None, filename=None, query=None):
        self.table = table
        self.query = ''
        self.mode = 0

        if self.debug:
            print('table = %s' % table)
            print('query_str = %s' % query)
            print('query_file = %s' % filename)

        if mode is DBTYPE_SQLLITE:
            self.named_param_before = ':'
            self.named_param_after = ''
            self.ignore_clause = 'or ignore '

        if table:
            return
        
        if query:
            self.query = query
            return 

        if filename:
            self.query = ''
            file_path = self.query_path + os.sep + filename
            if not os.path.exists(file_path):
                print("Failed to load sql file %s" % file_path)
            with open(file_path) as fp:
                self.query = fp.read()
            return 

        raise ValueError('Missing either table, filename or query')

    def format_sql_insert_values(self, fields):

        for field in fields:
            yield self.named_param_before + field + self.named_param_after

    def format_sql_update_values(self, fields):
        for field in fields:
            yield field + '=' +self.named_param_before + field + self.named_param_after

    def format_sql_values(self, fields):
        for field in fields:
            yield field + '=VALUES(' + field + ')'

    def join_col_val(self, fields, values):
        """join column names and values together with an equals sign"""
        sql = ''
        where_parts = []
        for field in fields:
            where_parts.append('%s=%s' % (field, values.get(field)))
        return ','.join(where_parts)

    def build_select(self, columns):
        if self.table is None:
            return self
        field_list = [field for field in columns]
        self.query = 'select %s from %s' % (', '.join(field_list), self.table)
        return self

    def build_insert(self, required, optional, values, on_duplicate = False):
        """ start an insert statement"""
        if self.table is None:
            return self
        field_list = [field for field in required]
        for field in optional:
            if values.get(field):
                field_list.append(field)
        value_list = [field for field in self.format_sql_insert_values(field_list)]
        self.query += 'insert %sinto %s (%s) VALUES (%s)' % (
            self.ignore_clause if self.expect_duplicates is True else '',
            self.table, 
            ','.join(field_list), 
            ', '.join(value_list))
        if on_duplicate is True:
            self.query += self.build_on_duplicate(field_list)
        return self


    def build_on_duplicate(self, fields):
        """join column names and values together with an equals sign for insert"""
        sql = ''
        where_parts = []

        field_list = [field for field in self.format_sql_values(fields)]
        return ' on duplicate key update %s' % ','.join(field_list)


    def build_delete(self):
        if self.table is None:
            return self
        self.query += 'delete from %s ' % self.table
        return self

    def build_update(self, required, optional, values):
        if self.table is None:
            return self
        fields = [item for item in required]
        for item in optional:
            if values.get(item):
                fields.append(item)
        self.query += 'update %s set %s' % (self.table, ','.join(self.format_sql_update_values(fields)))
        return self

    def build_where(self, where=None, where_columns=None, params=None):
        """build where conditions dynamically insert the columns to test and invalidate missing params"""
        if where:
            self.query += ' where ' + where
            return self
        if not (where_columns and params):
            return self
        where_conditions = []
        for where_column in where_columns:
            current_column = where_column.split('.')[-1] # account for tables names in where column
            if params.get(current_column) is None:
                where_conditions.append(where_column + '=' + where_column)
            else:
                where_conditions.append(where_column + "=" +self.named_param_before + current_column + self.named_param_after)
        if where_conditions:
            self.query += ' where ' + ' AND '.join(where_conditions)
        return self
    
    def build_group(self, grouping):
        """build grouping"""
        if not grouping:
            return self
        self.query += ' GROUP BY ' + ', '.join(grouping)
        return self
    
    def build_limit(self, page=0, limit=25, enabled = False):
        if enabled is False:
            return self
        start = (int(page) - 1) * int(limit)
        if start < 0:
            start = 0
        """build where conditions dynamically insert the columns to test and invalidate missing params"""
        self.query += ' LIMIT %s, %s' % (start, limit)
        return self

    def __str__(self):
        return self.query

    def finish(self):
        return self.query
