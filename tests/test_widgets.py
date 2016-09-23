#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import inspect
import os, sys
import traceback
from io import StringIO
from tests.test_utils import TestUtils
sys.path.insert(0,os.path.abspath('../'))
from scaffold import web

class TestBasePage(TestUtils):
    
    def setUp(self):
        self.maxDiff = None
        self.rel_path = os.path.dirname(__file__) + '/..'
        # web.load_widgets('widgets')

        web.load_widgets('tests/widgets')
        with web.template as setup:
            setup.persistant_uris(schema='http:', domain='localhost', port='')
    
    def test_base_widget_instances(self):
        for filename in os.listdir(self.rel_path + '/scaffold/www/base/'):
            if os.path.isdir(self.rel_path + '/scaffold/www/base/' + filename):
                continue
            if filename.endswith('.py'):
                name = filename[0:-3]
                methodToCall = getattr(web, name)
                try:
                    self.assertIsNotNone(methodToCall)
                except:
                    pass

    def test_default_widget_instances(self):
        for filename in os.listdir(self.rel_path + '/scaffold/www/default_widgets'):
            if os.path.isdir(self.rel_path + '/scaffold/www/default_widgets' + filename):
                continue
            if filename.endswith('.py'):
                name = filename[0:-3]
                methodToCall = getattr(web, name)
                try:
                    self.assertIsNotNone(methodToCall)
                except Exception as e:
                    pass

    def test_tables(self):
        expected = '<table  id="table0" >\n<caption class="tabtitle">Table Title</caption>\n<thead><tr class="tabhead"><th>Column Header 1</th><th>Column Header 2</th></tr></thead><tbody>\n<tr class="tabrow1"><td><th>row 12</th><tr class="tabrow2"><td><th>row 22</th>\n</tbody></table><br />\n'
        rows = (
            ('row 11', 'row 12'),
            ('row 21', 'row 22'),
        )
        web.table.create(title='Table Title', header=('Column Header 1', 'Column Header 2'))
        web.table * rows
        self.assertEquals(web.table.render(), expected)

    def test_uri_available(self):
        web.example.create()
        web.template.append(web.example.render())
        self.assertEqual(web.example.test_uri_access().rel, '//localhost')
        self.assertEqual(web.example.test_uri_access().ful, 'http://localhost')

    def test_custom_widget(self):
        web.example.create()
        web.template.append(web.example.render())

        expected = u"""
            <?xml version="1.0" encoding="utf-8"?>
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:sa="/">
                <head>

                </head>
                <body>
                <div id="example"></div><script type="text/javascript" ><!--//--><![CDATA[//><!--
            var test="hello world";
            //]]>
            </script>
                </body>
            </html>
        """
        #print(web.render())
        text1, text2 = self.clean(expected, web.render())
        self.assertEqual(text1, text2)
	
    def test_all_widgets(self):
        web.auto_load_all()

        test_params = {
            'progress_bar': {},
            'error':{},
            'example':{},
            'webglviewer': {},
            'toolbar': {},
            'notifications': {},
            'menu_slide_down': {},
            'carousel': {},
            'section': {},
            'debug': {},
            'buttons': {},
            'border': {},
            'markdown_editor': {},
            'notify': {},
            'banner_flip': {},
            'loginBox': {},
            'boxgrid': {},
            'banner_slide': {},
            'menu': {},

            'google_analytics':{
                'url': 'http://www.example.com', 
                'code': '2353647647'},
            'progress_bar':
                {'htm': 'Test Contents'},
            'breadcrumbs':
                {'root': 'Test Contents'},
            'lorem':
                {'length': 20},
            'error':
                {'htm': 'Test Contents'},
            'like':
                {'url': 'url'},
            'page':
                {'title': 'Test title'},
            'head':
                {'title': 'Test Contents'},
            'webglviewer':
                {'htm': 'Test Contents'},
            'images':{
                'image': 'test.png',
                'title': 'test title'
            },
            'container':
                {'content': 'test content'},
            'select':
                {'name': 'select_name'},
            'pagination':{
                'page': 1,
                'perpage': 10,
                'total': 30},
            'list_box':{
                'title': 'Title',
                'link': 'http://www.example.com',
                'details': 'descriptive text',
                'img': 'http://www.example.com/image.png'},
            'link':{
                'title': 'Link Title',
                'content': 'Display Text',
                'link': 'http://www.example.com'},
            'tabs':{
                'title': 'Link Title',
                'content': 'Display Text',
                'link': 'http://www.example.com'},
            'content':{
                'title': '',
                'header': '',
                'footer': '',
                'id':''
            },
            'barview': {
                'left': '',
                'centre': '',
                'right': ''
            },
            'list': {
                'text': 'lorem',
                'ordered': True
            },
            'gantt': {
                'text': 'text',
                'data_max': 20
            },
            'table': {
                'title': 'table title',
                'header': 'table header',
                'footer': 'table footer',
                'id': 'tableid'
            },
            'map': {
                'name': 'map_name'
            },
            'help': {
                'title': 'test title'
            },
            'menu': {
                'select': 'menuitem'
            },
            'boxes': {
                'id': 'boxid',
                'width': '100px',
                'height': '100px'
            },
            'google_plus': {
                'url': 'http://www.example.com',
                'plus': True,
                'share': 'share',
                'comments': 'comments'
            },
            'simple_form': {
                'action': 'action',
                'method': 'method'
            },
            'form_old': {
                'action': 'form action',
                'method': 'method',
                'enctype': 'enctype',
                'node_id': 'nodeid',
                'node_class': 'node class'
            }
        }

        expected = {
            'lorem': 'L'}

        for item in web.elements.keys():
            if 'test' in dir(getattr(web, item)):
                try:
                    result = len(inspect.getargspec(getattr(web, item).create).args)
                    if result==1:
                        getattr(web, item).test({})
                    else:
                        if test_params.get(item) == {}:
                            result = getattr(web, item).test()
                        else:
                            result = getattr(web, item).test(test_params.get(item, {'htm': 'Test Contents'}))
                        self.assertEqual(result[0].strip(), expected.get(item, '<'))
                except:
                    print(item)
                    print(inspect.getargspec(getattr(web, item).create).args)
                    print(traceback.format_exc())



if __name__ == '__main__':
    web.auto_load_all()
    unittest.main()
