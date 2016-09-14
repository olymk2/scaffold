import os
import sys
from .sql import query, query_builder
from .database import db as dataset
from .helper import required_values

class insert_data(query):
    on_duplicate = False

    def on_duplicate(self):
        self.on_duplicate = True
        return self

    def query(self):
        required_values(self.data, required=self.required)
        query_file = self.query_file
        query_str = self.query_str
        if type(self.query_file) is list:
            query_file = self.query_file[self.query_offset]
        if type(self.query_str) is list:
            query_str = self.query_str[self.query_offset]

        query = query_builder(mode=dataset.dbtype, table=self.table, filename=query_file, query=query_str) \
            .build_insert(required=self.required, optional=self.columns_optional, values=self.data, on_duplicate=self.on_duplicate)

        if self.debug is True:
            query_string = query.finish()
            print("\n%s\n%s" % (query_string, self.data))
            return query_string
        return query.finish()

    def execute(self, data, fetch_last_id=True):
        self.set(data)
        self.clean_data()
        with dataset() as database:
            database.execute(self.query(), self.data)
            self.query_offset += 1
            if  fetch_last_id is True:
                return database.last_id()
        return None
