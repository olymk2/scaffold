#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys

sys.path.insert(0,os.path.abspath('../'))
from scaffold.builder.minify import generate_static_content
from tests.test_utils import TestUtils


class TestBasePage(TestUtils):
    def test_minify_folder(self):

        self.rel_path = os.path.dirname(__file__) 
        generate_static_content(self.rel_path + '/resources/static/', '/tmp/static/')
        self.assertTrue(os.path.exists('/tmp/static/images/badges/founder.png'))
        #self.assertTrue(os.path.exists('/tmp/static/images/sprites/sprites1_32x32x.png'))
        #self.assertTrue(os.path.exists('/tmp/static/css/sprites/sprites1_32x32x.css'))
        self.assertTrue(os.path.exists('/tmp/static/css/default.css'))
        self.assertTrue(os.path.exists('/tmp/static/js/default.js'))


if __name__ == '__main__':
    unittest.main()
