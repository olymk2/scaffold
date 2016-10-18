#import required files
import os,sys
import tempfile
import webbrowser

#append this to module path so we can load from the parent directory
sys.path.insert(0,os.path.abspath('../../'))
from scaffold import web

# setup the default scripts and uri path
#with web.template as setup:
#    setup.persistent_header('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>')
#    setup.persistant_uris(**{'schema': 'file://', 'domain': os.path.abspath('../../scaffold'), 'static': 'www/default_widgets'})

#generate the main content of the page here
web.simple_form.create(action='/post', method='post')
web.simple_form.append(input_type="text", input_name="test_input_01", label="example text", values='foo bar')
web.simple_form.append(input_type="textarea", input_name="notes", label="notes", values='foo bar')
web.simple_form.append(input_type="email", input_name="test_input_02", label="example text")
web.simple_form.append(input_type="select", input_name="test_select_01", label="example text", values='example')
web.simple_form.append(input_type="select", input_name="test_select_02", label="example text", values=(('one', 'one'), ('two', 'two')))
web.simple_form.append(input_type="select", input_name="test_select_02", label="example text", values=('one', 'two', 'three'))
web.simple_form.append(input_type="submit", input_name="test_input_02", label="example text", values='submit')


#append the html into the document body
web.template.body.append(web.simple_form.render())

#nothing special dump content to a file and open in browser
f = tempfile.NamedTemporaryFile(delete=False)
f.write(web.render().encode('UTF-8'))
f.close()
webbrowser.open_new_tab('file:///'+f.name)
