#import required files
import os,sys
import tempfile
import webbrowser

#append this to module path so we can load from the parent directory
sys.path.insert(0,os.path.abspath('../'))
from scaffold.web import web as html

#the heart of the system
web=html()
web.document_root=os.path.dirname(__file__)

#set the default theme folder
web.template.theme_full_path=os.path.abspath('../')+os.sep+'themes'+os.sep+'default'+os.sep

#generate the main content of the page here
web.page.header('Hello World Header')
web.page.section('Hello World Body Text')

#append the html into the document body
web.template.body.append(web.page.render())

#nothing special dump content to a file and open in browser
f = tempfile.NamedTemporaryFile(delete=False)
f.write(web.render().encode('UTF-8'))
f.close()
webbrowser.open_new_tab('file:///'+f.name)
