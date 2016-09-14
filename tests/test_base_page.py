#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys
sys.path.insert(0,os.path.abspath('../'))
from scaffold import web
from test_utils import TestUtils

class TestBasePage(TestUtils):
    def setUp(self):
        with web.template as setup:
            setup.persistant_uris(schema='http:', domain='localhost', port='')


    def test_match(self):
        #~ t = web.render()

        with open('./resources/base_page.htm') as htm:
            htm.seek(0)
            text1, text2 = self.clean(htm.read(), web.render())
            self.assertEqual(text1, text2)
            #~ self.assertMultiLineEqual(t, htm.read())

if __name__ == '__main__':
    unittest.main()
