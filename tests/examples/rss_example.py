import os,sys
import datetime
import tempfile
import webbrowser

#append this to module path so we can load from the parent directory
sys.path.insert(0,os.path.abspath('../'))
sys.path.append(os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../'))
from scaffold.rss import rss
print dir(rss)

rss_builder = rss()
rss_builder.create('title', 'link', 'description')
rss_builder.channel_image('http://www.example.com/image.jpg')
items = []
items.append(['title01', 'link01', 'description01', datetime.datetime.now(), ['test']])
items.append(['title02', 'link02', 'description02', datetime.datetime.now(), ['test']])
items.append(['title03', 'link03', 'description03', datetime.datetime.now(), ['test']])
rss_builder * items

print rss_builder.render()
