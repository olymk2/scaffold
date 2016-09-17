#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys
from io import open

sys.path.insert(0,os.path.abspath('../'))
from scaffold import web
from scaffold.readers.markdown_reader import markdown_reader
from tests.test_utils import TestUtils

class TestBasePage(TestUtils):
    
    def setUp(self):
        with web.template as setup:
            pass
        web.template.append(
            markdown_reader().
            create('./tests/resources/markdown_reader.md').
            render()
        )

    def test_markdown_reader(self):
        with open('./tests/resources/markdown_page.htm', encoding='UTF-8') as htm:
            text1, text2 = self.clean(htm.read(), web.render())
            self.assertEqual(text1, text2)

if __name__ == '__main__':
    unittest.main()
