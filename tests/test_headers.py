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

with web.template as setup:
    setup.persistent_header(header_include[0])
    setup.persistant_uris(schema='https:', domain='test.com', port='5000')
    setup.header.append(non_persistent_header_include[0])


#~ from scaffold import web

class TestDataSetup(unittest.TestCase):
    def setUp(self):
        with web.template as setup:
            setup.persistent_header(header_include[0])
            setup.persistant_uris(schema='https:', domain='test.com', port='5000')
            setup.header.append(non_persistent_header_include[0])

    def test_headers_persist_between_renders(self):
        self.assertEqual(header_include, web.template.template_global_header)

    def test_nonpersistant_headers_do_not_persist_between_renders(self):
        self.assertEqual(header_include, web.template.template_global_header)

    def test_uris_persist(self):
        self.assertEqual(web.template.uri.rel, '//test.com:5000')
        self.assertEqual(web.template.uri.ful, 'https://test.com:5000')
        web.render()
        
        # confirm uris are still correct and not reset to defaults
        self.assertEqual(web.template.uri.rel, '//test.com:5000')
        self.assertEqual(web.template.uri.ful, 'https://test.com:5000')


if __name__ == '__main__':
    unittest.main()
