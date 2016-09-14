import os
import sys
from .sql import query, query_builder
from .database import db as dataset
from .helper import required_values

class delete_data(query):
    #~ required = {'id'}

    def query(self):
        query = query_builder(mode=dataset.dbtype, table=self.table, filename=self.query_file, query=self.query_str) \
            .build_delete() \
            .build_where(where=self.sql_where, where_columns=self.columns_where, params=self.data)
        return query.finish()

    def execute(self, data=None):
        self.set(data)
        with dataset() as database:
            database.execute(self.query(), self.data)
            return database.last_id()
