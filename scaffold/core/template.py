import os
from .uri import uri_path
from .site import base_site

class base_template(base_site):
    """ layout the html page insert javascript files create header etc """
    template_start = ("<?xml>\n")
    template_end = "\n"

    document = {
        'header': [],
        'footer': [],
        'body': []
    }
    document_text = ''
    document_encoding = 'utf-8'

    #~ template_encoding = 'utf-8'
    template_global_header = []
    template_global_body = []
    template_global_footer = []
    
    order = ('start', 'finish', 'header', 'body', 'footer')

    title = "Missing Title"

    path_absolute = '//path.absolute'
    absolute_path = os.path.abspath('./') + os.sep

    # cache settings start
    cache = 0
    cache_loaded = False
    cache_filename = None
    cache_folder = 'cache'
    cache_path = absolute_path + cache_folder + os.sep

    def __init__(self):
        self.document = {}
        self.document_text = ""
        self.template_global_header = []
        self.template_global_body = []
        self.template_global_footer = []
        self.reset()

    def reset(self, full=True):
        self.document['header'] = list(self.template_global_header)
        self.document["body"] = []
        self.document['footer'] = list(self.template_global_footer)

    def append(self, text):
        return self.document["body"]

    def __setattr__(self, key, value):
        if hasattr(self, key):
            super(base_template, self).__setattr__(key, value)
        else:
            self.document[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return getattr(self, key)
        else:
            return self.document[key]

    def disable_cache(self):
        self.cache = 0
        self.cache_loaded = False
        self.cache_filename = None

    def enable_cache(self, filename):
        self.cache = 1
        self.cache_loaded = False
        self.cache_filename = filename

    #enable cache to set filename
    def load_cache(self):
        path = self.cache_path + self.cache_filename
        self.cache_loaded = False
        try:
            if os.path.exists(path):
                fp = open(path, 'r')
                self.document_text = fp.read()
                fp.close()
                self.cache_loaded = True
        except:
            self.document_text = ''
            self.cache_loaded = False

        #reverse the logic so we can just do if load_cache
        return not self.cache_loaded

    #enable cache to set filename
    def save_cache(self):
        if self.cache_filename != None and self.cache_loaded == False and self.cache == 1:
            fp = open(self.cache_path + self.cache_filename, 'w')
            fp.write(self.document.encode(self.document_encoding))
            fp.close()

    def generate(self):
        #if the document has content then its been previously populated via cache or by user maybe
        self.document_text = self.template_start
        if self.cache_loaded is False:
            self.document_text += self.header_end
            self.document_text += "\n".join(self.document['body'])
            self.document_text += "\n".join(self.document['header'])
            self.document_text += "\n".join(self.document['footer'])
        self.document_text += self.template_end

    def render(self, reset=False):
        """ pass in true to clear everything """
        self.generate()
        self.save_cache()
        if reset:
            self.reset(True)
        else:
            self.reset(False)
        return self.document_text
