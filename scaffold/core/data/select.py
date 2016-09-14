import os
import sys
from .sql import query, query_builder
from .database import db as dataset
from .helper import required_values

class select_data(query):
    pagination_rows = 10
    limit_enabled = True
    count_rows = True
    grouping = []
    columns = {'*'}

    def __init__(self, data=None, page=0, limit_enabled=True):
        if data is None:
            data = {}
        if not isinstance(data, dict):
            sys.exit('data needs to be a dict!')
        self.page = page
        self.total_rows = 0
        self.data = data
        self.limit_rows = limit_enabled
        #required_values(self.data, required=self.required)

    def execute(self, data):
        self.set(data)
        with dataset() as database:
            return database.execute(self.query(), self.data)

    def update_values(self, data):
        self.data = data
        #required_values(self.data, required=self.required)

    def query(self, one_record=False):
        required_values(self.data, required=self.required)
        if one_record:
            self.limit_rows = False
        query = query_builder(mode=dataset.dbtype, table=self.table, filename=self.query_file, query=self.query_str) \
            .build_select(columns=self.columns) \
            .build_where(where=self.sql_where, where_columns=self.columns_where, params=self.data) \
            .build_group(self.grouping) \
            .build_limit(page=self.page, limit=self.pagination_rows, enabled=self.limit_enabled)
        if self.debug is True:
            query_string = query.finish()
            print("\n%s\n%s" % (query_string, self.data))
            return query_string
        return query.finish()

    def get(self):
        with dataset() as database:
            return database.fetchone(self.query(True), values=self.data)

    def __iter__(self):
        with dataset() as database:
            for row in database.fetchall(self.query(), values=self.data):
                yield row
            if self.count_rows is True:
                if dataset.dbtype==0:
                    self.total_rows = database.fetchone('SELECT FOUND_ROWS();').get('FOUND_ROWS()', 0)
    
    def get_total(self):
        return self.total_rows
