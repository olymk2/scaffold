#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import tempfile
import webbrowser
import unittest

sys.path.insert(0,os.path.abspath('../'))
from scaffold import web

header_include = ['<link rel="stylesheet" id="navigationCss" href="/static/template/default.css" media="" type="text/css" />']
persistent_header_include = ['<link rel="stylesheet" id="navigationCss" href="/static/template/persist.css" media="" type="text/css" />']
non_persistent_header_include = ['<link rel="stylesheet" id="navigationCss" href="/static/template/dontpersist.css" media="" type="text/css" />']

class TestDataSetup(unittest.TestCase):
    def setUp(self):
        web.load_widgets('tests/widgets')
        with web.template as setup:
            setup.persistent_header(header_include[0])
            setup.persistant_uris(schema='https:', domain='test.com', port='5000')
            setup.header.append(non_persistent_header_include[0])

    def test_widget_uri(self):
        self.assertEqual('//test.com:5000/image.jpg', web.example.uri.add_domain('/image.jpg'))

    def test_convert_relative_to_full(self):
        self.assertEqual('//test.com:5000/image.jpg', web.template.uri.add_domain('/image.jpg'))

    def test_dont_convert_full(self):
        self.assertEqual('//test.com:5000/image.jpg', web.template.uri.add_domain('//test.com:5000/image.jpg'))

    def test_full_url_is_not_made_relative_scheme_url(self):
        self.assertEqual('http://test.com:5000/image.jpg', web.template.uri.add_domain('http://test.com:5000/image.jpg'))




if __name__ == '__main__':
    unittest.main()
