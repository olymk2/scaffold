#import required files
import os,sys
import tempfile
import webbrowser

#append this to module path so we can load from the parent directory
sys.path.append(os.path.abspath('../'))
from scaffold.web import web as html

#the heart of the system
web=html()
web.document_root=os.path.dirname(__file__)
web.template.enable_cache('helloworld_cache')

if web.template.load_cache():
	#set the default theme folder
	web.template.theme_full_path=os.path.abspath('../')+os.sep+'themes'+os.sep+'default'+os.sep

	#these allow you to load in a static file to header and footer 
	web.template.load_header()
	web.template.load_footer()

	#generate the main content of the page here
	web.page.header('Hello World Header')
	web.page.section('Hello World Body Text')

	#append the html into the document body
	web.template.body.append(web.page.render())
#web.template.clear_cache()
#nothing special dump content to a file and open in browser
f = tempfile.NamedTemporaryFile(delete=False)
f.write(web.render().encode('UTF-8'))
f.close()
webbrowser.open_new_tab('file:///'+f.name)
