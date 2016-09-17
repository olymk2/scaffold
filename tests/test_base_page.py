#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys
from io import open
sys.path.insert(0,os.path.abspath('../'))
from scaffold import web
from tests.test_utils import TestUtils

class TestBasePage(TestUtils):
    def setUp(self):
        with web.template as setup:
            setup.persistant_uris(schema='http:', domain='localhost', port='')

    def test_match(self):
        with open('./tests/resources/base_page.htm', encoding='UTF-8') as htm:
            htm.seek(0)
            text1, text2 = self.clean(htm.read(), web.render())
            self.assertEqual(text1, text2)

if __name__ == '__main__':
    unittest.main()
