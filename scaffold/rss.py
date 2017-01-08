import time
import cgi

from email.utils import formatdate
from scaffold.template import page_template

class rss(object):
    rsshead=""
    rssfoot=""
    rssbody=""

    def __init__(self,page_path={}):
        self.javascript=""
        self.htmlhead=""
        self.htmlfoot=""
        self.htmlbody=""
        
        self.items=[]
        self.details=[]

    def create(self, title, link, description):
        self.channel_image = ''
        self.channel_image_title = ''
        self.channel_image_link = ''
        
        self.title = title
        self.link = link
        self.description = description

    def __mul__(self, items):
        for row in items:
            self.append(*row)

    def __add__(self, items):
        for row in items:
            self.append(*row)

    def reset(self):
        self.title = ''
        self.link = ''
        self.description = ''
        self.channel_image = None

    def escape(self, text):
        return cgi.escape(text)

    def channel(self,title,link,description):

        rss=(   u'\t\t<title>%s</title>\n' % self.escape(title),
                u'\t\t<link>%s</link>\n' % self.escape(link),
                u'\t\t<description>%s</description>\n' % self.escape(description))
                #'<language>en-us</language>\n',
                #'<pubDate>Tue, 10 Jun 2003 04:00:00 GMT</pubDate>\n',

                #'<lastBuildDate>Tue, 10 Jun 2003 09:41:01 GMT</lastBuildDate>\n',
                #'<docs>http://blogs.law.harvard.edu/tech/rss</docs>\n',
                #'<generator>Weblog Editor 2.0</generator>\n',
                #'<managingEditor>editor@example.com</managingEditor>\n',
                #'<webMaster>webmaster@example.com</webMaster>\n')
        self.rssfeed=''.join(rss)

    def channel_image(self, url, title=None, link=None):
        self.channel_image = url
        self.channel_image_title = title if title else self.title
        self.channel_image_link = link if link else self.link

    def append(self, title, link, description, date, image, tags=[]):
        categorys = []
        for cat in tags:
            if cat:
                categorys.append(u'\t\t\t<category>%s</category>\n' % cat)
        if image:
            image = u'\t\t\t<media:thumbnail url="%s" />\n' % image
        rss = (   
            u'<item>\n',
            u'\t\t\t<title>%s</title>\n' % self.escape(title),
            u'\t\t\t<link>%s</link>\n' % self.escape(link),
            u'\t\t\t<guid isPermaLink="false">%s</guid>\n' % self.escape(link),
            u'\t\t\t<description>%s</description>\n' % self.escape(description),
            u'\t\t\t<pubDate>%s</pubDate>\n' % formatdate(time.mktime(date.timetuple())),
            u''.join(categorys),
            image,
            u'\t\t</item>\n')
        self.items.append(u"".join(rss))

    def sub_element(self, parent, node, text):
        node = etree.SubElement(parent, node)
        node.text = text
        return node

    def render(self):
        #~ channel_node = etree.Element("channel")
        #~ node = self.sub_element(channel_node, "title", self.title)
        #~ node = self.sub_element(channel_node, "link", self.link)
        #~ node = self.sub_element(channel_node, "description", self.description)
        rss = [
            u'\t\t<title>%s</title>\n' % self.escape(self.title),
            u'\t\t<link>%s</link>\n' % self.escape(self.link),
            u'\t\t<description>%s</description>\n' % self.escape(self.description)]

        if self.channel_image:
            rss.append(u'\t\t<image>\n')
            rss.append(u'\t\t\t<url>%s</url>\n' % self.escape(self.channel_image))
            rss.append(u'\t\t\t<title>%s</title>\n' % self.escape(self.channel_image_title))
            rss.append(u'\t\t\t<link>%s</link>\n' % self.channel_image_link)
            rss.append(u'\t\t</image>\n')

        self.rssfeed = u''.join(rss)

        txt2 = u''
        for item in self.items:
            txt2 += u'\t\t' + item + ''
        u'\t\t' + txt2         
        
        rss = (
            u'<?xml version="1.0" encoding="utf-8"?>\n',
            u'<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">\n'
            u'\t<channel>\n',
            self.rssfeed,
            txt2,
            u'\t</channel>\n',
            u'</rss>')
        return u"".join(rss)
