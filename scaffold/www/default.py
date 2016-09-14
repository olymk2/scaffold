from io import StringIO
import sys
from ...core.widget import base_widget


class control(base_widget):  
    name = ''
    options = []
    text = ''
    
    #incremented on render
    count = 0
    indent = 0  # self.indent * "\t"
    
    renderMode = 0
    beenUsed = False  # this can be used to determine if a class has been used, useful for including stuff once only
    node_class = ''
    node_class_list = []
    node_id = ''

    # javascript includes or css, will go in the header
    includes = []
    
    #javascript code appended to footer
    script = []
    html = []
    namespace = 'sa'

    seperator = ''
    content = []
    def __init__(self, mode=0):
        self.content = []
        self.seperator = ''
        self.node_attrs = [
            ['id', None],
            ['class', None],
            ['title', None]]
        self.renderMode = mode
        self.beenUsed = True

    def __call__(self):
        self.reset()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def start(self):
        """ same as reset allows you to initialise and start using append in a loop"""
        self.content = []
        self.reset_attributes()

    def create(self):
        """ this is basically a start append call """
        self.content = []
        self.reset_attributes()

    def reset(self):
        """ reset append and attributes """
        self.reset_attributes()
        self.content = []
        self.seperator = ''
        return self

    def add_class(self, name, reset = False):
        """ append class to element """
        if reset is True:
            self.node_class_list = []
        self.node_class_list.append(name)

    def reset_attributes(self):
        """ reset id class title back to defaults """
        self.node_attrs = [
            ['id', None],
            ['class', None],
            ['title', None]]

    def get_attributes(self):
        """ get all attributes and there values and any additional attributes"""
        result = ' '
        for attr, value in self.node_attrs:
            if value is not None:
                result += attr + u'="' + value + u'" '
        return result

    def add_attributes(self,name, value):
        """ get all attributes and there values and any additional attributes"""
        self.node_attrs.append([name, value])
        return self

    def set_classes(self, name):
        """ add classes to root element """
        self.node_attrs[1][1] = name
        self.node_class_list = name
        return self

    def set_seperator(self, value):
        """ add classes to root element """
        self.seperator = value
        return self

    def get_class(self):
        return self.node_attrs[1][1]

    def get_id(self):
        """ return the current value of the root elements id
        Args:
            none
        Returns:
            unique id for the element
        """
        return self.node_attrs[0][1]

    def append(self, text):
        self.html.append(text)

    def __mul__(self, items):
        for row in items:
            self.append(*row)

    def __add__(self, items):
        for row in items:
            self.append(*row)

    def set_id(self, identity):
        """ set root element id attribute 
        Args:
            unique id of the element
        Returns:
            Nothing
        """
        self.node_attrs[0][1] = identity
        self.node_id = 'id="%s"' % identity
        return self

    #def parameters(self,id="",*options):
    #    self.name=id
    #    self.options=options

    def renderJscript(self):
        return ''

    def renderHead(self):
        return ''

    def renderBody(self):
        return ''

    def renderFoot(self):
        return ''

    def javascript(self):
        pass

    #alternate form colours
    def switch_form_style(self):
        if self.style=="formrow1":
            self.style="formrow2"
        else:
            self.style="formrow1"

    def read(self):
        return StingIO(self.render).read()

    def render(self):
        return "/n".join(self.html)
