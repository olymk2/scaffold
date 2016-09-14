#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

#~ import www
from .www import default_widgets
from .www import forms
from .www import base as default_nodes
from .www.encode.xmlstring import xml_string
from .template import page_template
from types import MethodType

# TODO add caching for pages added stub functions
class webpage(object):
    """Templating object responsible for compiling and outputting the pages document"""
    template = page_template()

    #0 = no cache loaded so we will need to create for next time
    cache = 1
    cache_loaded = 0
    cache_path = '/cache/'
    cache_file = None

    render_encodeing = 'utf-8'
    render_start = 0
    render_end = 0
    render_time = 0

    #html elements generated from classes will be stored here.
    elements = {}
    custom_widgets = None
    xmlstring = xml_string()
    indent = 0

    document_root = '/'
    module_paths = []

    def __init__(self, rendermode=0, cachemode=0, encoding='UTF-8'):
        self.render_start = time.time()

    def load_widgets(self, module_path):
        sub_module_list = [mod[0:-3] for mod in os.listdir(module_path) if mod.endswith('.py') and mod != '__init__.py']
        module_name = module_path.replace(os.sep, '.')
        self.custom_widgets = __import__(module_path, globals(), locals(), sub_module_list)
        #~ import sys;sys.exit(1)

    def __enter__(self):
        self.render_start = time.time()

    def __exit__(self):
        self.render_time = self.render_end - self.render_start
        
    def start(self):
        self.render_start = time.time()

    def load_modules(self, path):
        __import__()
        #for item in dir(forms):
        #    self.form_val[item] = item
    
    def widget(self):
        items = self.elements.keys()
        for a in self.elements.keys():
        #~ for widget_key in self.elements.keys():
            yield self.elements[a]
        
        #~ for widget in default_widgets.__dict__.keys():
            #~ yield default_widgets[widget]
        
        #~ for widget in forms.__dict__.keys():
            #~ yield forms[widget]

        #~ for widget in self.custom_widgets.__dict__.keys():
            #~ yield custom_widgets[name]

        #~ for widget in self.default_widgets.__dict__.keys():
            #~ yield default_widgets[name]

    def register(self):
        for name in www.__dict__:
            self.__dict__[name] = www.base.__dict__[name]

        for name in widgets.__dict__:
            self.__dict__[name] = widgets.__dict__[name]

    def auto_load_all(self):
        for widget in default_nodes.__dict__.keys():
            if hasattr(getattr(default_nodes, widget), 'control'):
                self.auto_load(widget)
        
        for widget in default_widgets.__dict__.keys():
            if hasattr(getattr(default_widgets, widget), 'control'):
                #~ print widget
                self.auto_load(widget)
        #~ if default_widgets.__dict__.get(name, None):


    def auto_load(self, name):
        """ import module by name looking in known import paths 
        Args:
            name of class that your loading
        Returns:
            Nothing
        """
        #~ try:
        if default_nodes.__dict__.get(name, None):
            self.elements[name] = default_nodes.__dict__[name].control()
            return 

        if forms.__dict__.get(name, None):
            self.elements[name] = forms.__dict__[name].control()
            return 

        # users custom widgets let these override the built in widgets
        if self.custom_widgets and self.custom_widgets.__dict__.get(name, None):
            self.elements[name] = self.custom_widgets.__dict__[name].control()
            return

        if default_widgets.__dict__.get(name, None):
            self.elements[name] = default_widgets.__dict__[name].control()
            return 

        print('no such widget %s' % name)

    def extend(self, item, partial):
        """Extend Web class with a new method adding a new parital

        Args:
            name of method.class that your attaching
        Returns:
            Nothing
        """
        self.elements[item] = partial

    def patch(self, name, func, method):
        """Extend Web class with a new method adding a new parital

        Args:
            name of class, new method name, method to patch
        Returns:
            Nothing
        """
        setattr(self.elements[name], func, MethodType(method, web.elements[name]))

    def __getattr__(self, name):
        """ call our function try auto loading if its not found """
        if self.elements.get(name):
            return self.elements[name]

        try:
            self.auto_load(name)
            return self.elements[name]
        except Exception as e:
            import traceback, sys
            print(traceback.print_exception(*sys.exc_info()))
            print('an error was found in %s - %s' % (name, e))
            return None

    def generate_files(self):
        """Generate a default css file"""
        with open(self.template.css_path, 'w') as fp:
            for item in self.elements.keys():
                for css in self.elements[item].css:
                    #~ self.template.javascript_includes.append(css)
                    fp.write(css)

    def get_includes(self):
        """ loop over template javascript includes and append to template """
        for item in self.elements.keys():
            if self.elements[item].count != 0:
                #header javascript
                for include in self.elements[item].includes:
                    self.template.javascript_includes.append(include)

                #footer inline javascript, 
                if self.elements[item].js:
                    self.template.jscript.append(js)

                #obsolete script and use js above instead
                for script in self.elements[item].script:
                    self.template.jscript.append(script)

                #append to the footer, usefull for last minute things like javascript
                for footer in self.elements[item].footer:
                    self.template.footer.append(footer)

    def render(self):
        """ render out all html text 

        Args:
            name of method.class that your attaching
        Returns:
            Nothing
        """
        self.get_includes()
        self.render_end = time.time()
        self.render_time = self.render_end - self.render_start
        self.render_start = self.render_end
        return self.template.render().encode('UTF-8')

    def preview(self):
        """ dump content to a temporary file and open in browser """
        try:
            import tempfile
            import webbrowser
            f = tempfile.NamedTemporaryFile(delete=False)
            f.write(self.render().encode('UTF-8'))
            f.close()
            webbrowser.open_new_tab('file:///'+f.name)
            return True
        except:
            return False
