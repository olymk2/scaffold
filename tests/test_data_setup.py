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

query_builder.query_path = os.path.abspath('./data/sql/')

database = {'host':'test_simple_querys.db', 'type': 'sqllite', 'charset': 'utf-8'}

db.config(database)

class delete(delete_data):
    table = 'users'
    required = {'id'}
    columns = {}

class select(select_data):
    table = 'users'
    required = {}
    columns = {'id', 'email', 'password', 'username', 'first_name', 'last_name', 'created', 'modified'}
    # debug = True

class select_simple_group(select_data):
    table = 'categories'
    required = {}
    columns = {'name', 'total'}
    grouping = {'name'}


class select_str_query(select_data):
    table = 'users'
    required = {'id'}
    query_str = 'select  id, username, email from users'
    columns = {'id', 'email', 'password', 'username', 'first_name', 'last_name'}
    columns_where = {'users.username'}

class select_str_join_query(select_data):
    required = {'id'}
    query_str = 'select users.id, username, email from users left join user_details on users.id = user_details.user_id'
    columns = {'id', 'email', 'password', 'username', 'first_name', 'last_name', 'description'}
    columns_where = {'users.id'}

class create(insert_data):
    # debug = True
    table = 'users'
    required = {'email', 'password', 'username', 'first_name', 'last_name', 'created'}
    columns = {'email', 'password', 'username', 'first_name', 'last_name', 'created'}
    columns_optional = {'profile_image'}

    def calculated_data(self):
        return {'created': time.strftime('%Y-%m-%d %H:%M:%S')}

class create_user_details(insert_data):
    #~ debug = True
    table = 'user_details'
    required = {'user_id', 'description'}
    columns = {'user_id', 'description'}
    #~ columns_optional = {'profile_image'}

class create_category(insert_data):
    #~ debug = True
    table = 'categories'
    required = {'user_id', 'name', 'total'}
    columns = {'user_id', 'name', 'total'}
    #~ columns_optional = {'profile_image'}


class update(update_data):
    table = 'users'
    required = {'id'}
    columns_where = {'id'}
    columns = {'email', 'password', 'username', 'first_name', 'last_name', 'modified'}
    columns_optional = {'email', 'password', 'username', 'first_name', 'last_name'}
    # debug = True
    def calculated_data(self):
        return {'modified': time.strftime('%Y-%m-%d %H:%M:%S')}

class update_last_login(update_data):
    table = 'users'
    required = {'user_id'}
    debug = True
    query_str = "update `users` set `last_login`=now() where id=%(user_id)s"
    #~ columns = {'id'}

class TestDataSetup(unittest.TestCase):
    def setUp(self):
        db.config(database)
        if os.path.exists(database.get('host')):
            os.remove(database.get('host'))
        with db() as data:
            data.execute('CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(30), last_name VARCHAR(30), username VARCHAR(30), email VARCHAR(100), password varchar(30), created TIMESTAMP, modified TIMESTAMP)')
            create().execute({
                    'email': 'sprite@test.com',
                    'username': 'sprite',
                    'password': 'jhgjhgjhg',
                    'first_name': 'sprite',
                    'last_name': 'fuzzie'
            })

        with db() as data:
            data.execute('CREATE TABLE user_details(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, description TEXT)')
            create_user_details().execute({
                    'user_id': '1',
                    'description': 'my descriptive text'
            })

        with db() as data:
            data.execute('CREATE TABLE categories(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, name VARCHAR(255), total INT)')
            create_category().execute({'user_id': '1','name': 'fruit', 'total': '4'})
            create_category().execute({'user_id': '1','name': 'fruit', 'total': '7'})
            create_category().execute({'user_id': '1','name': 'veg', 'total': '3'})
            create_category().execute({'user_id': '1','name': 'pasta', 'total': '8'})

if __name__ == '__main__':
    unittest.main()
