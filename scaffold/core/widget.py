from io import StringIO
from .uri import uri_path
from .site import base_site

class base_widget(base_site):
    css_row = 'row'
    css_column = 'col s12'
    
    js = None  # inline javascript for this widget
    css = None  # styles for this widget, usefull to create a default stylesheet
    script = []  # javascript for this widget

    includes = []  # any file based includes
    footer = []  # anything to append to the footer like javascript
    count = 0

    node = u''
    content = []

    seperator = "\n"

    def create(self):
        self.count += 1
        return self

    @classmethod
    def new(cls, *args):
        """initalise the class with some default values and render the result"""
        return cls().create(*args)

    @classmethod
    def test(cls, *args):
        """initalise the class with some default values and render the result"""
        tst = cls()
        tst.create(*args)
        return tst.render()

    def __init__(self):
        self.content = []
        self.footer = []

    def __call__(self):
        self.reset()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """ clear out the default values"""
        self.reset()

    def __mul__(self, items):
        if type(items[-1]) in (str, bytes):
            for row in items:
                self.append(row)
            return 

        for row in items:
            self.append(*row)

    def __add__(self, items):
        self.concat(items)

    def concat(self, text):
        """dont append join the value onto the previous value"""
        self.content[-1] += text
        return self

    def reset(self):
        pass
    
    def get_script(self):
        return "<script type=\"text/javascript\">%s</script>" % "\n\t".join(self.script)

    def append(self, text):
        """append a new value to the list"""
        self.content.append(text)
        return self

    def read(self):
        return StringIO(self.render())

    def render(self):
        self.count += 1
        return "/n".join(self.content)


class base_widget_extended(base_widget):

    def __init__(self):
        self.content = []
        self.node_attrs = [
            ['id', None],
            ['class', None],
            ['title', None]]

    def reset_attributes(self):
        """ reset id class title back to defaults """
        self.node_attrs = [
            ['id', None],
            ['class', None],
            ['title', None]]
        return self

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

    def add_class(self, name):
        """ append class to element """
        self.node_attrs[1][1] = name
        return self

    def set_classes(self, name):
        """ add classes to root element """
        self.node_attrs[1][1] = name
        return self

    def set_id(self, identity):
        """ set root element id attribute 
        Args:
            unique id of the element
        Returns:
            Nothing
        """
        self.node_attrs[0][1] = identity
        #~ self.node_id = 'id="%s"' % identity
        return self
    
    def get_id(self):
        return self.node_attrs[0][1]
