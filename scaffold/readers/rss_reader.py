import os
import lxml
import pytz
from io import StringIO, BytesIO
import datetime
import requests
import functools
import requests.exceptions

from operator import itemgetter
from lxml import etree
from lxml.html.clean import Cleaner

namespaces = {
    'openSearch': "http://a9.com/-/spec/opensearchrss/1.0/",
    'blogger': "http://schemas.google.com/blogger/2008",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'slash': "http://purl.org/rss/1.0/modules/slash/",
    'content': "http://purl.org/rss/1.0/modules/content/",
    'taxo': "http://purl.org/rss/1.0/modules/taxonomy/",
    'dc': "http://purl.org/dc/elements/1.1/",
    'syn': "http://purl.org/rss/1.0/modules/syndication/",
    'admin': "http://webns.net/mvcb/",
    'feedburner': "http://rssnamespace.org/feedburner/ext/1.0",
    'wfw': "http://wellformedweb.org/CommentAPI/",
    'dc': "http://purl.org/dc/elements/1.1/",
    'atom': "http://www.w3.org/2005/Atom",
    'sy': "http://purl.org/rss/1.0/modules/syndication/",
    'slash': "http://purl.org/rss/1.0/modules/slash/",
    'atom': "http://www.w3.org/2005/Atom",
    'content': "http://purl.org/rss/1.0/modules/content/",
    'media': "http://search.yahoo.com/mrss/",
}


from email.utils import parsedate_tz, mktime_tz


class feed_reader:
    """parse a list of feeds and return details as dictionary data"""
    #create the html cleaner, this is to clean out unwanted html tags in the description text
    #page_structure=True,remove_unknown_tags=True
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'}
    html_cleaner = Cleaner()
    html_cleaner.javascript = True 
    html_cleaner.style = True
    html_cleaner.remove_tags = ['script', 'iframe', 'link', 'style', 'img', 'div']
    #~ html_cleaner.allow_tags = ['a', 'p', 'strong']

    filter_by_date_expire = datetime.datetime.now() - datetime.timedelta(days=int(1.5*365)) #  1 and a half years ago

    html_img_cleaner = Cleaner(allow_tags=['img'], remove_unknown_tags=False)
    html_img_cleaner.allow_tags = ['img']

    html_parser = lxml.etree.HTMLParser()
    xml_parser = lxml.etree.XMLParser(remove_blank_text=True, ns_clean=True, encoding='utf-8')

    enable_date_filter = True

    def __init__(self, feed_details, timeout=5):
        self.results = {}
        pos = 1
        for feed_info in feed_details:
            if not feed_info.get('id'):
                feed_info['id'] = pos
            self.url = feed_info.get('url')
            self.author = feed_info.get('author')
            self.tags = feed_info.get('tags', None)
            if feed_info.get('url').startswith(('http:', 'https:')):
                try:
                    response = requests.get(feed_info.get('url'), stream=True, timeout=timeout, headers=self.headers)
                except (requests.exceptions.Timeout, Exception) as e:
                    continue
                if response.headers.get('content-encoding') == 'gzip':
                    response.raw.read = functools.partial(response.raw.read, decode_content=True)
                try:
                    self.feed = lxml.etree.parse(response.raw, self.xml_parser)
                except Exception as e:
                    print(e)
                    continue
            else:
                with open(os.path.abspath(feed_info.get('url')), 'r') as file_stream:
                    try:
                        self.feed = lxml.etree.parse(file_stream, self.xml_parser)
                    except Exception as e:
                        continue
            self.feed = self.feed.getroot()

            # rss feed defaults
            self.channel_image = self.fetch_node_text(self.feed, 'channel/image/url', '')
            self.parse_feed(feed_info)
            pos += 1

    def convert_rfc822_to_datetime(self, rfcdate):
        """rss uses rfc822 dates so lets convert them to datetime for use later"""
        if len(rfcdate):
            parsed_rfcdate = parsedate_tz(str(rfcdate))
            if not parsed_rfcdate:
                return None
            return datetime.datetime.fromtimestamp(
                mktime_tz(parsed_rfcdate), pytz.utc).replace(tzinfo=None)
        return None

    def clean_up_text(self, text):
        """strip out any dirty tags like <script> they may break the sites"""
        if text is None:
            return ''
        cleaned_html = self.html_cleaner.clean_html(text)

        # parse large text seperately
        if len(text) > 600:
            description = lxml.etree.parse(BytesIO(cleaned_html), self.html_parser)
            root = description.getroot()
            build = BytesIO()
            for node in root[-1][-1].iter():
                #skip any nodes with no text
                if node.text is None and node.tail is None:
                    continue
                # we may want to do some other node checks here 
                # perhaps count paragraphs, html layout changes a lot
                if node.tag == 'br':
                    return build
                else: 
                    if node.tag == 'a' and node.text is None:
                        build.write(node.tail)
                    else:
                        a = etree.tostring(node)
                        build.write(etree.tostring(node))

        return self.html_cleaner.clean_html(text)

    def fetch_image_from_node_text(self, text):
        description = lxml.etree.parse(BytesIO(text), self.html_parser)
        for image in description.xpath('.//img'):
            return image.get('src')
        return None

    def fetch_image(self, node):
        """Try and get an image from an item in the feed, use various fall back methods"""
        image = node.xpath('media:thumbnail', namespaces=namespaces)
        if image:
            return image[0].get('url', u'')

        # no media:thumbnail so lets try and grab an image from content:encoded
        image = node.xpath('content:encoded', namespaces=namespaces)
        if image:
            image = self.fetch_image_from_node_text(image[0].text.encode('utf8'))
            if image:
                return image

        # final attempt at getting an image from the item using description
        result = self.fetch_node_text(node, 'description')
        if result:
            image = self.fetch_image_from_node_text(result)
            if image:
                return image

        # no image so lets fall back to the channel image if it exists
        return self.channel_image


    def fetch_node_text(self, node, name, default=u''):
        """fetch the text from the node we are given, we are working in unicode
        so decode byte strings to unicode""" 
        result = node.xpath('./%s' % name)
        if result is None or len(result) is 0:
            return default

        if type(result[-1].text) is str:
            return result[-1].text.encode('utf-8')
        else:
            return result[-1].text

    def fetch_node_attribute(self, node, name, attribs, default):
        result = node.xpath('./%s' % name)
        if result:
            return result.get(attribs, '')
        else:
            return default

    def format_author(self, author):
        """extract the authors name from the author text node"""
        if author:
            return author.split('(')[-1].strip(')')
        return 'Anonymous'

    def filter_by_tags(self, node, tags=None):
        """filter the feed out by category tag, if no tags assume its pre filtered"""
        if self.tags is None:
            return True
        for category in node.xpath('./category', namespaces=namespaces):
            if category.text.lower() in self.tags:
                return True
        return False

    def filter_by_date(self, date):
        """filter the feed out by date"""
        if self.enable_date_filter is False:
            return True
        if date > self.filter_by_date_expire:
            return True
        return False

    def parse_feed(self, feed=None):
        """Parse the items in the feed, filter out bad data and put in defaults"""
        if feed is None:
            feed = {}
        for item in self.feed.xpath('.//item', namespaces=namespaces):
            date = self.convert_rfc822_to_datetime(self.fetch_node_text(item, 'pubDate'))
            if self.filter_by_date(date) and self.filter_by_tags(item):
                author = self.format_author(self.fetch_node_text(item, 'author', self.author))
                self.results.setdefault(author, []).append({
                    'id': feed.get('id', 1),
                    'title': self.fetch_node_text(item, 'title'),
                    'date': date,
                    'url': self.fetch_node_text(item, 'link'),
                    'author': author,
                    'image': self.fetch_image(item),
                    'description': self.clean_up_text(self.fetch_node_text(item, 'description'))})

        #order authors articles by date
        for author in self.results.keys():
            self.results[author] = sorted(self.results[author], key=itemgetter('date'), reverse=True)

    def alternate_dict_and_sort_by_list_item_key(self, dict_of_lists, sort_key='date'):
        """ take a dictonary of ordered lists, step through each row and sort the current
        item position in each list and yield the result.
        
        basically gives the ordering of date while stepping through the blog entries to make it fair
        for people who do not blog often. """
        
        
        longest_list_length = max([len(dict_of_lists[d]) for d in dict_of_lists.keys()] + [0])
        
        # order each feed by date, newest date at the end of the list so it can be poped
        for author in dict_of_lists:
            dict_of_lists[author].sort(key=itemgetter('date'), reverse=False)

        # now iterate through author lists, popping the first elements and order the current item 
        # from each list by date
        for i in range(0, longest_list_length):
            # get first value from each key, and order the list by sort key which is date by default
            feed_row = [d.pop() for d in dict_of_lists.values() if d]
            results = sorted(feed_row, key=itemgetter(sort_key), reverse=True)
            for item in results:
                yield item

    def __iter__(self):
        """return results ordered by date"""
        for author in self.alternate_dict_and_sort_by_list_item_key(self.results):
            yield author
