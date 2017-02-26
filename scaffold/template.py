import os

from .core.uri import uri_path
from .core.site import base_site
from .core.widget import base_widget
from .core.template import base_template

class page_template(base_template):
    """ layout the html page insert javascript files create header etc """
    #<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:sa="/">
    template_start = (u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
                    "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.1//EN\" \"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd\">\n"
                    "<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" xmlns:sa=\"/\">\n\t<head>\n\t\t")
    template_end = u"\n\t</head>\n\t<body>\n\t"
    body_end = "\n\t</body>\n</html>\n\t"
    
    order = ('header', 'includes', 'javascript_includes', 'css_includes', 'jscript', 'body', 'footer')

    title = "Missing Title"
    id = ''

    path = '/'
    path_static = path + 'static/'
    
    #defaults
    template_global_header = [
    '<link rel="stylesheet" id="navigationCss" href="/static/css/default.css" media="" type="text/css" />',
    '<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>',
    '<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.2/angular.min.js"></script>']

    #path_static = path + 'static/'
    #css javascript template images
    path_template = path + 'static/templates/'

    #public images seperate from the theme
    path_image = path + 'static/images/' 
    path_theme = path + 'static/themes/'
    
    path_javascript = path +'js/' 
   
    #phasing out with path_ instead for consitancy
    absolute_path = os.path.abspath('./')+os.sep
    template_folder = 'static/template'
    css_path = template_folder + '/css'
    theme_folder = 'default'
    theme_absolute_path=template_folder + os.sep + theme_folder

    schema = 'http:'
    domain = '//127.0.0.1'
    rel_uri = '//127.0.0.1:5000'
    abs_uri = '%s//127.0.0.1:5000' % schema
    img_uri = domain


    #cache settings start
    cache = 0
    cache_loaded = False
    cache_filename = None
    cache_folder = 'cache'
    cache_path = absolute_path + cache_folder + os.sep

    def __init__(self):
        super(page_template, self).__init__()
        self.set_paths(self.path)
        #self.document = {}
        #self.document_text = ""

        # template code lines new replace self.document['attrib']
        js_include = []
        css_include = []
        js_script = []

    def __enter__(self):
        self.persistant_start()
        return self

    def __exit__(self, type, value, traceback):
        """ clear out the default values"""
        self.persistant_finish()
        return False

    def persistant_start(self):
        """This will reset the persistent header, its called when you use with via __enter__,
        by default this will include jquery and angular unless specified yourself"""
        self.template_global_header = []
        self.template_global_footer = []
        return self

    def persistant_finish(self):
        self.reset(full=True)
        return self

    def persistent_header(self, text):
        """Add a header line which will persist accross pages
        Args: string line to store"""
        self.template_global_header.append(text)

    def persistent_footer(self, text):
        self.template_global_footer.append(text)

    def persistant_uris(self, **args):
        self.uri.update(**args)
        base_site.uri.update(**args) # = self.uri

    def set_paths(self, path='/'):
        # todo obsolete this in favor of persistent path
        page_template.path = path
        page_template.path_static + path + 'static/'

        #css javascript template images
        page_template.path_template = self.path_static + 'template/'
        page_template.path_javascript = self.path_static + 'js/'

        #public images seperate from the theme
        page_template.path_image = self.path_static + 'images/'
        page_template.path_theme =  self.path_static + 'themes/'

        base_widget.path_absolute = path

        self.set_cache_path()
        self.reset()

    def create(self, title, description=None, meta=[]):
        self.set_paths(page_template.path)
        self.document['header'].append('<title>%s</title>' % title)
        self.document['header'].append('<meta http-equiv="Content-Type" content="text/html; charset=%s">' % self.document_encoding)
        if description:
            self.document['header'].append('<meta property="description" name="description" content="%s" />' % description)
        for prop, value in meta:
            self.document['header'].append('<meta property="%s" name="%s" content="%s" />' % (prop, prop, value))

    def set_cache_path(self, path=None):
        if path:
            page_template.cache_path = absolute_path + cache_folder + os.sep
        try:
            if not os.path.exists(page_template.cache_path):
                os.makedirs(page_template.cache_path)
        except:
            print('Failed to create cache folder')

    def clear_cache(self):
        for filename in os.listdir(self.cache_path):
            os.unlink(page_template.cache_path + os.sep + filename)

    def reset(self, full=True):
        self.document['header'] = list(self.template_global_header)
        self.document["jscript"] = []

        self.document["includes"] = ''
        #~ self.document["htmhead"] = []
        self.document["body"] = []

        if full:
            self.document["javascript_includes"] = []
            self.document["css_includes"] = []

            #~ self.document["htmfoot"] = ""
        self.document['footer'] = list(self.template_global_footer)

    def script(self, text):
        self.document['header'].append(text)

    def append(self, text):
        return self.document["body"].append(text)

    def load_header(self):
        self.reset()
        self.document_text = ''
        self.document['header'].append(self.template_start)
        fp = open(self.theme_absolute_path + 'header.html')
        self.document['header'].append(fp.read())
        fp.close()
        self.document['header'].append(self.template_end)

    def load_footer(self):
        fp = open(page_template.theme_absolute_path + 'footer.html')
        self.document['footer'].append(fp.read())
        fp.close()

    def join(self, dictonary):
        for k in self.keys():
            if k in dictonary.keys():
                try:
                    self.document[k] += dictonary[k]
                except:
                    print("incompatible type" + str(k) + str(dictonary))

    def generate(self):
        #if the document has content then its been previously populated via cache or by user maybe
        self.document_text = self.template_start
        if self.cache_loaded is False:
            for css in self.document["css_includes"]:
                self.document['header'].append('<link rel="stylesheet" id="navigationCss" href="' + css + '" media="" type="text/css" />\n')
            self.document_text += "\n\t\t".join(self.document['header'])
            self.document_text += "\n\t\t".join(self.document["javascript_includes"])

            self.document_text += self.document['includes']
            #~ self.document_text += "\n".join(self.document['htmhead'])
            #for j in self.document['jscript'].keys():

            self.document_text += self.template_end
            #~ self.document_text += self.document['htmbody']
            #~ print(self.document['body'])
            #~ print("\n".join(self.document['body']))
            self.document_text += "\n".join(self.document['body'])
            #~ self.document_text += self.document['htmfoot']
            self.document_text += '\n'.join(self.document['footer'])
            if self.document['jscript']:
                self.document_text += "<script type=\"text/javascript\" ><!--//--><![CDATA[//><!--\n"
                #htmout+=self.template['jscript']+
                self.document_text += "\n\n".join(self.document['jscript'])
                self.document_text += "\n//]]>\n</script>\n"
            self.document_text += self.body_end

    def render(self, reset=False):
        """ pass in true to clear everything """
        self.generate()
        self.save_cache()
        if reset:
            self.reset(True)
        else:
            self.reset(False)
        return self.document_text

    def read(self):
        return self.document_text
