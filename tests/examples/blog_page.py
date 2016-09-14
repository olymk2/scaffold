#import required files
import os,sys
import tempfile
import webbrowser

#append this to module path so we can load from the parent directory
sys.path.insert(0,os.path.abspath('../'))
sys.path.append(os.path.abspath('../'))
from scaffold.web import web as html



#the heart of the system
web=html()
web.document_root=os.path.dirname(__file__)
#set the default theme folder
web.template.theme_full_path=os.path.abspath('../')+os.sep+'themes'+os.sep+'blog'+os.sep
web.template.css_includes.append(web.template.theme_full_path+'main.css')

web.menu.create('/', 'leftNav')
web.menu.append('menu 1', '#menu1')
web.menu.append('menu 2', '#menu2')
web.menu.append('menu 3', '#menu3')
web.menu.append('menu 4', '#menu4')

web.template.body.append(web.menu.render())

#generate the main content of the page here
#web.page.header('Blog Entry Title')
#web.container.create('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea reb')
#web.container.append('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea reb')
#web.page.section(web.container.render())

web.images.create("test.jpg")
web.link.create("comments", 'C', "#comments")

#import ipdb; ipdb.set_trace()

web.container.create(node_class="date")

web.div.create('01', node_class='day')
web.container.add(web.div.render())

web.div.create('Apr', node_class='month')
web.container.add(web.div.render())

web.container.create(web.container.render(), node_class="heading")
web.div.create(web.link.render(), node_class="comment")
web.container.add(web.div.render())
web.container.add('<h1 class="title">Hello World !</h1>')

web.page.create(web.container.render(), 'page')
web.page.section(web.container.render())
web.page.append('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea reb')
web.google_plus.create('http://www.example.org/', True, True, True)
web.page.footer(web.google_plus.render())

web.google_analytics.create('http://www.example.com','UA-XXXXXXXX-X')

web.google_analytics.render()
#append the html into the document body
web.template.body.append(web.page.render())


#nothing special dump content to a file and open in browser
f = tempfile.NamedTemporaryFile(delete=False)
f.write(web.render().encode('UTF-8'))
f.close()
webbrowser.open_new_tab('file:///'+f.name)
