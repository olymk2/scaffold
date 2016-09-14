import os
import sys
from .sql import query, query_builder
from .database import db as dataset
from .helper import required_values

class update_data(query):
    
    def query(self):
        query = query_builder(mode=dataset.dbtype, table=self.table, filename=self.query_file, query=self.query_str) \
            .build_update(self.columns, self.columns_optional, self.data) \
            .build_where(where=self.sql_where, where_columns=self.columns_where, params=self.data)
        if self.debug is True:
            query_string = query.finish()
            print("\n%s\n%s" % (query_string, self.data))
        return query.finish()

    def execute(self, data):
        self.set(data)
        with dataset() as database:
            database.execute(self.query(), self.data)
            return database.last_id()
