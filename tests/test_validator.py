#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import unittest

sys.path.insert(0,os.path.abspath('../'))
from scaffold.core.validate import validate

class TestBasePage(unittest.TestCase):

    def setUp(self):
        self.validator = validate()

    def test_valid_network_addresses(self):
        self.assertEqual(
            self.validator.validate("1.100.80.12","n3.n3.n3.n3"),
            (1, '1.100.80.12', '1.100.80.12'))
        self.assertEqual(
            self.validator.validate("128.10.6.2","n3.n3.n3.n3"),
            (1, '128.10.6.2', '128.10.6.2'))
        self.assertEqual(
            self.validator.validate("00:10:FA:F1:4D:FF","h"),
            (2, '0', "00:10:FA:F1:4D:FF"))

    def test_valid_dates(self):
        self.assertEqual(
            self.validator.validate("06/08/2008","d10"),
            (2, '06', '06/08/2008'))
        self.assertEqual(
            self.validator.validate("06/08/2008","d2s-d2s-d4"),
            (2, '06', '06/08/2008'))

        self.assertEqual(
            self.validator.validate("1995-10-11","d*s-d*s-d*"),
            (1, '1995-10-11', '1995-10-11'))

    def test_valid_text(self):
        self.assertEqual(
            self.validator.validate("hello world", "T*"),
            (1, "hello world", "hello world"))
        
        self.assertEqual(
            self.validator.validate("qwerty234","l*"),
            (2, "qwerty", "qwerty234"))
        
        self.assertEqual(
            self.validator.validate("test Text Field ___", "T*"),
            (1, 'test Text Field ___', 'test Text Field ___'))

    def test_valid_number(self):
        self.assertEqual(
            self.validator.validate("1234567891234567891234567891234567891234567891", "n10"),
            (2, "1234567891", "1234567891234567891234567891234567891234567891"))

        self.assertEqual(
            self.validator.validate("234", "n"),
            (2, '2', '234'))

        self.assertEqual(
            self.validator.validate("234x453", "n*"),
            (2, '234', '234x453'))


    def test_post_codes(self):
        self.assertEqual(
            self.validator.validate("tn13jh", "l*n*l*"),
            (1, 'tn13jh', 'tn13jh'))

        self.assertEqual(
            self.validator.validate("tn1 3jh", "l*n* n*l*"),
            (1, 'tn1 3jh', 'tn1 3jh'))

    def test_valid_custom(self):
        self.assertEqual(
            self.validator.validate("qwerty234", "l*n"),
            (2, 'qwerty2', 'qwerty234'))

        self.assertEqual(
            self.validator.validate("qwerty234qwe34","t*n*lll"),
            (1, 'qwerty234qwe34', 'qwerty234qwe34'))

        self.assertEqual(
            self.validator.validate("text+-:text","n[t+-]*n"),
            (2, 'text+-', 'text+-:text'))

        self.assertEqual(
            self.validator.validate("te*st","[t*]*"),
            (1, 'te*st', 'te*st'))


if __name__ == '__main__':
    unittest.main()

