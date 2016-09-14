#import required files
import os,sys
import tempfile
import inspect
import webbrowser

#append this to module path so we can load from the parent directory
sys.path.insert(0,os.path.abspath('../../'))
sys.path.append(os.path.abspath('../../'))
from scaffold import web
from scaffold.core.widget import base_widget
#~ from scaffold.www.default import html_ui

#bw = base_widget()


ignore_methods = set()
ignore_methods.update([m[0] for m in inspect.getmembers(base_widget(), predicate=inspect.ismethod)])
#~ ignore_methods.update([m[0] for m in inspect.getmembers(html_ui(), predicate=inspect.ismethod)])

#the heart of the system
#~ web=html()
web.document_root=os.path.dirname(__file__)
#set the default theme folder
web.template.theme_full_path=os.path.abspath('../')+os.sep+'themes'+os.sep+'default'+os.sep
web.auto_load_all()

#these allow you to load in a static file to header and footer 
#web.template.load_header()
#web.template.load_footer()

#normally this will look for the defaults.css file in your theme we are not serving files so set local path 
web.template.css_includes.append('file:///'+web.template.theme_full_path+'default.css')

#generate the main content of the page here
web.page.header('Hello World Extended Header')

examples = {}


def get_inherited_class(klass, method_name):
    for superclass in klass.__bases__:
        next_superclass = get_inherited_class(superclass, method_name)
        if next_superclass is not None:
            return next_superclass
        for supermethod_name, supermethod in inspect.getmembers(superclass, inspect.ismethod):
            if supermethod_name == method_name:
                return superclass
    return None


def annotate_methods(klass):
    annotated_methods = []
    # loop over class methods
    for method_name, method in inspect.getmembers(klass, inspect.ismethod):
        annotated_method = {
            'method_name': method_name,
            'method': method,
            'method_mode': 'default',
            'class_name': klass.__name__
        }

        # loop over the parent classes
        for superclass in klass.__bases__:
            # recall annotate until ewe get to the top level parent then work back down
            for annotated_supermethod in annotate_methods(superclass):
                if method_name == annotated_supermethod['method_name']:
                    # the method is inherited or overridden - but from where?
                    inherited_class = get_inherited_class(klass, method_name)
                    annotated_method['class_name'] = inherited_class.__name__
                    if method == annotated_supermethod['method']:
                        annotated_method['method_mode'] = 'inherited'
                    else:
                        annotated_method['method_mode'] = 'overridden'

        annotated_methods.append(annotated_method)
    return annotated_methods

def get_methods(obj):
    method_ids = []
    # collect method ids of parent methods
    for filter in obj.__class__.__bases__:
        for method_name, method in inspect.getmembers(filter, predicate=inspect.ismethod):
            method_ids.append(id(method.im_func))

    # loop over class methods and compare the metho ids to the ids in the parent
    # if they match this method came from the parent so skip, also skip private methods
    for method_name, method in inspect.getmembers(obj, predicate=inspect.ismethod):
        method_id = id(method.im_func)
        if method_id in method_ids:
            continue
        if method_name.startswith('__'):
            continue
        yield {
            'method_name': method_name,
            'method_params': [param for param in method.func_code.co_varnames if param != 'self'],
            'method_help': method.func_code.__doc__,
            'method': method}

for item in web.elements.keys():
    htm = '<h1>method ' + item+'</h1><ol>'
    print 'class = %s' % item
    print 'Parents = %s ' % str(web.elements[item].__class__.__bases__)
    print 'Parents = %s ' % str(web.elements[item].__class__.__doc__)
    #for m in dir(html.elements[item]):
    for m in get_methods(web.elements[item]):
    #~ for m in annotate_methods(html.elements[item].__class__):
        #~ if m['method_mode'] in ['default', 'overridden']:
        print "\t%s %s" % (m['method_name'], m['method_params'])
        print "\t%s" % (m['method_help'])
        htm += '<li>'+m['method_name']+'</li>'
    htm += '</ol>'
    web.container.append(examples.get(item,'no example yet coming soon'))
    htm += web.container.render()
    web.page.section(htm)
    
web.template.body.append(web.page.render())

#nothing special dump content to a file and open in browser
f = tempfile.NamedTemporaryFile(delete=False)
f.write(web.render().encode('UTF-8'))
f.close()
webbrowser.open_new_tab('file:///'+f.name)
