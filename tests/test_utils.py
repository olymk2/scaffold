#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys
from StringIO import StringIO

sys.path.insert(0,os.path.abspath('../'))
from scaffold import web

class TestUtils(unittest.TestCase):
    """Utility functions for running tests"""
    def setUp(self):
        with web.template as setup:
            pass
            
    def clean(self, text1, text2):
        """remove blank space and carriage returns, we may not care about these in the test results"""
        text1 = StringIO(text1)
        text2 = StringIO(text2)
        
        text1_clean = ''
        for line in text1.readlines():
            text1_clean += line.strip()
        
        text2_clean = ''
        for line in text2.readlines():
            text2_clean += line.strip()
        return text1_clean.replace("\n", ''), text2_clean.replace("\n", '')
