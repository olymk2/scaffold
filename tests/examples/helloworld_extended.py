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


web.menu.create('/')
web.menu.append('home', '/')
web.menu.append('test', '/test/')
web.page.section(web.menu.render())

#these allow you to load in a static file to header and footer
#web.template.load_header()
#web.template.load_footer()

#normally this will look for the defaults.css file in your theme we are not serving files so set local path
web.template.css_includes.append('file:///'+web.template.theme_full_path+'default.css')
web.template.create('hello world extended')
#generate the main content of the page here
web.page.header('Hello World Extended Header')
web.page.section('Hello World Extended Body Text')
web.page.append('test append')

web.link.set_classes(('testclass','one',))
web.link.create('title','link content','www.google.co.uk')
web.link.create('title','link content','www.google.co.uk')
web.link.create('title','link content','www.google.co.uk')

web.page.section(web.link.render())
#example of creating a table
web.table.create('My Table Title',('Column 1','Column 2','Column 3','Column 4','Column 5'))
for row in range(0,6):
    web.table.append([str(row),'a','b','c','d'])

##actually lets modify the rows for the table, just an example to show it possible as long as render has not been called
for row in web.table:
    row[2]='<b>'+row[2]+'</b>'


web.page.section(web.table.render())

web.list.create()
web.list.append('Initial Applicaton')
web.list.append('Draw Points')
web.list.append('Setup Camera')
web.list.append('Draw Lines')
web.page.section(web.list.render())

web.barview.create('left', 'middle', 'right')
web.page.section(web.barview.render())

#append the html into the document body
web.template.body.append(web.page.render())


#nothing special dump content to a file and open in browser
f = tempfile.NamedTemporaryFile(delete=False)
f.write(web.render().encode('UTF-8'))
f.close()
webbrowser.open_new_tab('file:///'+f.name)
