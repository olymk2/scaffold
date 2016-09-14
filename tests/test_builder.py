#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys, shutil
from StringIO import StringIO
sys.path.insert(0,os.path.abspath('../'))
from scaffold import web
from scaffold.builder.__main__ import main as builder_main
from test_data_setup import * 


class AttributeDict(dict): 
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class TestBuilder(TestDataSetup):
    
    def setUp(self):
        self.path = '/tmp/example_project'
    
    def test_generate_new_project_in_explicit_path(self):
        builder_main(AttributeDict({
            'cmd':'init',
            'path':'/tmp',
            'name': 'example_project',
            'verbose': False}))
        path = '/tmp/example_project'
        
        self.assertTrue(os.path.exists(path + '/site/static/css'))
        self.assertTrue(os.path.exists(path + '/debian/control'))
        self.assertTrue(os.path.exists(path + '/debian/rules'))
        
        self.assertTrue(os.path.exists(path + '/site/views'))
        self.assertTrue(os.path.exists(path + '/site/config/settings.py'))
        self.assertTrue(os.path.exists(path + '/site/index.py'))
        
        #shutil.rmtree(path)
    
    def test_generate_new_project_in_current_path(self):
        path = '/tmp/example_project'
        builder_main(AttributeDict({
            'cmd':'init',
            'verbose': False}))
        
        
        self.assertTrue(os.path.exists(path + '/site/static/css'))
        self.assertTrue(os.path.exists(path + '/debian/control'))
        self.assertTrue(os.path.exists(path + '/debian/rules'))
        
        self.assertTrue(os.path.exists(path + '/site/views'))
        self.assertTrue(os.path.exists(path + '/site/config/settings.py'))
        self.assertTrue(os.path.exists(path + '/site/index.py'))
        
        #shutil.rmtree(path)

    def test_generate_migrations(self):
        path = '/tmp/example_project/migrations'
        builder_main(AttributeDict({
            'cmd':'migrate',
            'export': True,
            'type': 'sqllite',
            'host': 'test_import_migrations.db',
            'path': path,
            'verbose': False}))

    def test_run_migrations(self):
        builder_main(AttributeDict({
            'cmd':'migrate',
            'install': True,
            'type': 'sqllite',
            'host': 'test_import_migrations.db',
            'verbose': False}))

    def test_minify(self):
        builder_main(AttributeDict({
            'cmd':'minify',
            'source': self.path + '/static_resources',
            'target': self.path + '/static',
            'verbose': False}))

        self.assertTrue(os.path.exists(self.path + '/site/static/css/default.css'))
        # todo generate spritesheet generator


    def test_default_widget_instances(self):
        pass


if __name__ == '__main__':
    unittest.main()
