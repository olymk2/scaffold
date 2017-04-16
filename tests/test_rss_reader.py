#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os, sys, shutil
import tempfile
import webbrowser

sys.path.insert(0, os.path.abspath('./'))
from scaffold.readers.rss_reader import feed_reader
#from test_utils import TestUtils

rss_feeds = [{
        'id': 'a',
        'author':'Author 01',
        'url': './tests/test_data/rss_feed_digitaloctave.rss'
    }, {
        'author':'Author 02', 'tags': ['tech'], 
        'url': './tests/test_data/rss_feed_test_media_thumbs.rss'
    }, {
        'author':'Author 02', 'tags': ['tech'], 
        'url': './tests/test_data/rss_feed_xkcd.rss'
    }, {
        'author':'Author 03', 
        'url': 'https://blog.digitaloctave.com/rss.xml'
    }, {
        'author':'Author 03', 
        'url': './tests/test_data/rss_feed_invalid.rss'
    }, {
        'author':'Author 04', 
        'url': './tests/test_data/rss_feed_no_tags.rss'
    }]


class TestBasePage(unittest.TestCase):
    # def setUp(self):
    #     self.feeds = feed_reader(rss_feeds)

    def test_rss_reader(self):
        self.feeds = feed_reader(rss_feeds)
        for row in self.feeds:
            self.assertNotEqual('', row.get('author'))
            self.assertNotEqual('', row.get('id'))

    def test_image_via_media_attribute(self):
        self.feeds = feed_reader([{
            'author':'Author 02',
            'url': './tests/test_data/rss_feed_test_media_thumbs.rss'
        }])
        for row in self.feeds:
            self.assertNotEqual('', row.get('author'))
            self.assertNotEqual('', row.get('id'))
            self.assertEquals('/media/post/robot-coming-together.full.jpg', row.get('image'))




if __name__ == '__main__':
    unittest.main()
