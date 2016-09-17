#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import unittest

sys.path.insert(0,os.path.abspath('../'))
from scaffold.core.data.database import db
from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder
from tests.test_data_setup import * 

query_builder.query_path = os.path.abspath('./data/sql/')

database = {'host':'test_simple_querys.db', 'type': 'sqllite'}

db.config(database)

class TestBasePage(TestDataSetup):

    def test_simple_insert_invalid_data(self):
        self.assertEqual(len([row for row in select()]), 1)

        create().execute({
                'email': u'ted[]dy@test.com',
                'username': u'te$£ddy',
                'password': u'hj()fdjh',
                'first_name': u'sp#~te',
                'last_name': u'fuz¬`|ie'
        })
        results = [row for row in select()]
        
        #make sure this column was updated automatically with python
        self.assertIsNotNone(results[0]['created'])
        
        #do we have a new row inserted ?
        self.assertEqual(len([row for row in results]), 2)

    def test_simple_insert(self):
        self.assertEqual(len([row for row in select()]), 1)

        create().execute({
                'email': 'teddy@test.com',
                'username': 'teddy',
                'password': 'hjskfdjh',
                'first_name': 'sprite',
                'last_name': 'fuzzie'
        })
        self.assertEqual(len([row for row in select()]), 2)

    def test_simple_update(self):
        create().execute({
                'email': 'teddy@test.com',
                'username': 'teddy',
                'password': 'hjskfdjh',
                'first_name': 'sprite',
                'last_name': 'fuzzie'
        })

        user = select().get()
        #make sure this column was updated automatically with python
        self.assertIsNone(user['modified'])

        updated_cols = ('username', 'email', 'password', 'first_name', 'last_name')
        update().execute({
                'id': '1',
                'username': 'teddy_modified',
                'email': 'teddy_modified@test.com',
                'password': 'hjskfdjh_modified',
                'first_name': 'sprite_modified',
                'last_name': 'fuzzie_modified'
        })
        user = select().get()

        #make sure this column was updated automatically with python
        count = len([row for row in updated_cols if 'modified' in user[row]])
        
        self.assertIsNotNone(user['modified'])
        self.assertEqual(count, 5)

    #~ def test_update_fixed_query(self):
        #~ update_last_login().execute({
            #~ 'user_id': '1'
        #~ })

    def test_get_record(self):
        user = select_str_query({'id': '1'}).get()

    def test_get_grouped_records(self):
        cats = [(row['name'], row['total']) for row in select_simple_group()]
        self.assertEquals(cats, [(u'fruit', 7), (u'pasta', 8), (u'veg', 3)])

    def test_select_varying_where(self):
        self.assertEqual(
            len([row for row in select_str_query({'id': '1'})]),
            1
        )
        self.assertEqual(
            len([row for row in select_str_query({'id': '1', 'username': 'sprite'})]),
            1
        )

    def test_select_with_duplicate_names(self):
        user = select_str_join_query({'id': '1'}).get()

    def test_simple_delete(self):
        delete().execute({'id': '1'})
        self.assertEqual(len([row for row in select()]), 0)


if __name__ == '__main__':
    unittest.main(buffer=False)

