#import required files
import os,sys
sys.path.insert(0,os.path.abspath('../'))
import flask


#append this to module path so we can load from the parent directory

from scaffold.web import web as html

html.template.path_javascript='themes'+os.sep+'js'+os.sep
#the heart of the system
web=html()
print '123'
web.document_root=os.path.dirname(__file__)
#set the default theme folder
#web.template.theme_full_path=os.path.abspath('../')+os.sep+'themes'+os.sep+'default'+os.sep
web.template.theme_full_path='themes'+os.sep+'default'+os.sep
web.template.path_javascript='themes'+os.sep+'js'+os.sep
images_path=os.path.abspath('../')+os.sep+'themes'+os.sep
web.template.set_paths('/themes/')

#these allow you to load in a static file to header and footer 
#~ web.template.load_header()
#~ web.template.load_footer()

#normally this will look for the defaults.css file in your theme we are not serving files so set local path 
web.template.css_includes.append(web.template.theme_full_path+'default.css')

#generate the main content of the page here
web.page.header('Hello World Extended Header')
web.page.section('Hello World Extended Body Text')

web.images.create('file:///'+images_path+'images/DSC_0191.JPG','example image').set_classes('img_background')
web.page.section(web.images.render())

web.menu.create('', '')
web.menu.append('title 1','http://www.google.co.uk')
web.menu.append('title2','http://www.google.co.uk')

web.page.section(web.menu.render())

#print dir(web.buttons)
web.buttons.append('/prev','/themes/img/player_rew.png','Previous','prev')
web.buttons.append('/play','/themes/img/player_play.png','Play','play')
web.buttons.append('/next','/themes/img/player_fwd.png','Next ','next')
web.page.section(web.buttons.render())

#generate volume bar
for v in (0,10,20,30,40,50,65,75,85,100):
    web.boxes.append('<span>'+str(v)+'</span>')

web.boxes.add_class('container')
web.page.section(web.boxes.render(),'volume')


#example of creating a table
web.table.create('My Table Title',('Column 1','Column 2','Column 3','Column 4','Column 5'))
for row in range(0,6):
    web.table.append((str(row),'a','b','c','d'))

web.pagination.create(10,100,1)
web.page.section(web.pagination.render())

count=0
for b in range(0,6):
    web.boxes.append('test box '+str(count))
    count=count+1
web.page.section(web.boxes.render())

web.page.section(web.paragraph.create(web.lorem.render()).render())
web.page.section(web.loginbox.render())

print dir(web.input)
#web.page.section(web.input.create('tezst','123').render())
web.upload.create('uploader')
web.page.section(web.upload.render())
web.page.section(web.table.render())
#append the html into the document body
web.template.body.append(web.page.render())




from flask import Flask
app = Flask(__name__, static_folder=os.path.abspath('../themes/'))

@app.route('/')
def hello_world():
    return web.render()

if __name__ == '__main__':
    app.run()
