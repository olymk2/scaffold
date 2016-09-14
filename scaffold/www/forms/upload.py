#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui
import sys

class control(html_form_ui):        
    mode="5"
    limit='1'
    id='upload'
    custom_message = 'Drop your image to upload here'

    def create(self, name, values=None, error=0):
        self.error = error
        self.name = name
        if values is None:
            self.values = {}
        else:
            self.values = values

    def custom_text(self, text):
        self.custom_message = text

    def javascript(self,id=None):
        if self.mode==5:
            return self.javascript_html5(id)
        else:
            return self.javascript_html5(id)

    #FIXME ajax uploader currently erroring on multiple large image uploads strangly in duplicates of two O.o
    def javascript_html5fileHandle(self,id):
        js=("function handleFile(file) {\n",
            "//console.log(file.target);\n",
            "console.log(file.target.file.type);\n",
            "console.log('image handle '+file.target.index);\n",

            "\t if(file.target.file.type.match(/application.*/)) {\n",
            "\t\t       alert('binary stl / application');\n",
            "\t\t       var contain = document.createElement(\"div\");\n",
            "\t\t       contain.id = 'fileupload'+file.target.index;\n", #file.target.readAsDataURL(file);\n",
            "\t\t       var img = document.createElement(\"img\");\n",
            "\t\t       img.id = 'imageupload'+file.target.index;\n", #file.target.readAsDataURL(file);\n",
            
            "\t\t       img.src = file.target.file.getAsDataURL(file.target.file);\n", #file.target.readAsDataURL(file);\n",            
            "\t\t       var progress = document.createElement(\"div\");\n",

            "\t\t       contain.classList.add(\"uploadPreview\");\n",
            "\t\t       progress.classList.add(\"progress\");\n",
            "\t\t       $(contain).append(progress);\n",
            "\t\t       $(contain).append(img);\n",
            "\t\t       $('.upload').append(contain);\n",
            "\t }\n",

            "\t if(file.target.file.type.match(/image.*/)) {\n",
            "\t\t       var contain = document.createElement(\"div\");\n",
            "\t\t       contain.id = 'fileupload'+file.target.index;\n", #file.target.readAsDataURL(file);\n",
            "\t\t       var img = document.createElement(\"img\");\n",
            "\t\t       img.id = 'imageupload'+file.target.index;\n", #file.target.readAsDataURL(file);\n",
            
            "\t\t       img.src = file.target.file.getAsDataURL(file.target.file);\n", #file.target.readAsDataURL(file);\n",            
            "\t\t       var progress = document.createElement(\"div\");\n",

            "\t\t       contain.classList.add(\"uploadPreview\");\n",
            "\t\t       progress.classList.add(\"progress\");\n",
            "\t\t       $(contain).append(progress);\n",
            "\t\t       $(contain).append(img);\n",
            "\t\t       $('.upload').append(contain);\n",
            "\t }\n",

            "\t if(file.type.match(/video.*/)) {\n",
            "\t     var video = document.createElement(\"video\");\n",
            "\t     video.setAttribute(\"autoplay\", true);\n",
            "\t     video.setAttribute(\"controls\", true);\n",
            "\t     var reader = new FileReader();\n",
            "\t     reader.onloadend = function() {\n",
            "\t         video.src = reader.result;\n",
            "\t     }\n",
            "\t     reader.readAsDataURL(file);\n",
            "\t     video.classList.add(\"obj\");\n",
            "\t     bag.insertBefore(video, bag.firstChild);\n",
            "\t     return true;\n",
            "\t }\n",

            "\t if(file.type.match(/audio/)) {\n",
            "\t     var audio = document.createElement(\"audio\");\n",
            "\t     audio.setAttribute(\"autoplay\", true);\n",
            "\t     audio.setAttribute(\"controls\", true);\n",
            "\t     var reader = new FileReader();\n",
            "\t     reader.onloadend = function() {\n",
            "\t         audio.src = reader.result;\n",
            "\t     }\n",
            "\t     reader.readAsDataURL(file);\n",
            "\t     audio.classList.add(\"obj\");\n",
            "\t     bag.insertBefore(audio, bag.firstChild);\n",
            "\t     return true;\n",
            "\t }\n",

            "\t if(file.type.match(/text.*/)) {\n",
            "\t     var txt = document.createElement(\"textarea\");\n",
            "\t     txt.cols = 35;\n",
            "\t     txt.rows = 15;\n",
            "\t     var reader = new FileReader();\n",
            "\t     reader.onloadend = function() {\n",
            "\t         txt.value = reader.result;\n",
            "\t     }\n",
            "\t     reader.readAsText(file);\n",
            "\t     txt.classList.add(\"obj\");\n",
            "\t     bag.insertBefore(txt, bag.firstChild);\n",
            "\t     return true;\n",
            "\t }\n",

            "\t var xhr = new XMLHttpRequest();\n",
            "\t xhr.upload.index=file.target.index;\n",
            

            #upload progress
            "\t xhr.upload.addEventListener('progress', function(event) {\n",
            "\t\t   if (event.lengthComputable) {\n",
            "\t\t\t     var percentage = Math.round((event.loaded * 100) / event.total);\n",
            "\t\t\t     if (percentage < 100) {\n",
            "\t\t\t\t       $('#fileupload'+event.target.index+'>.progress').css('width',percentage+'%');",
            "\t\t\t\t       $('#fileupload'+event.target.index+'>.progress').html(percentage+'%');",
            "\t\t\t     }\n",
            "\t\t   }\n",
            "\t }, false);\n\n",

            #load event or upload complete
            "\txhr.addEventListener('load', function(event){\n",
            #"\t\t  console.log('complete--#fileupload'+event.target.index+ '> .progress');\n"
            "\t\t   $('#fileupload'+event.target.index+ '> .progress').css('width','100%');\n",
            "\t\t   $('#fileupload'+event.target.index+ '> .progress').html('100%');\n",
            "\t\t   $('#fileupload'+xhr.upload.index).html(event.target.responseText);\n",
            "\t\t   console.log('#fileupload'+xhr.upload.index);\n",
            "\t\t   console.log(event.target.responseText);\n",
            "\t}, false);"

            "\t var boundary='multipartformboundary' + (new Date).getTime();\n",  
            "\t xhr.open('POST', '/ajax/%s/upload');"%self.plugin,
            "\t xhr.setRequestHeader('Content-Type', 'multipart/form-data; boundary='+boundary);",

            "\t var data = '--'+boundary+ '\\r\\nContent-Disposition: form-data; name=\"page\"\\r\\n\\r\\n%s\\r\\n';\n"%self.plugin,
            "\t data += '--'+boundary+ '\\r\\nContent-Disposition: form-data; name=\"subpage\"\\r\\n\\r\\nupload\\r\\n';\n",

            "\t data += '--'+boundary+ '\\r\\nContent-Disposition: form-data; name=\"user_file'+file.target.index+'\"; filename=\"' +file.target.file.fileName+ '\"\\r\\n';\n",
            "\t data += 'Content-Type: application/octet-stream\\r\\n\\r\\n';\n",
            "console.dir(file.target);"
            "\t data += file.target.file.getAsBinary()+'\\r\\n';",
            "\t data += '--'+boundary+'--\\r\\n\\r\\n';\n",
            
            "\t xhr.sendAsBinary(data);\n\n",
            "\t return false;\n",
            "}\n")
        return "".join(js)

    def javascript_html5(self,id=None):
        js=("var uploadcount=0;\n",
            "var uploadlimit='%s';\n"%self.limit, 
            "function upload(event) {\n",
            #"\t        var dt = event.dataTransfer;\n",
            "\t     var files = event.dataTransfer.files;\n",

            #"\t\tevent.stopPropagation();\n",
            "\t     event.preventDefault();\n",

            #handle binary files

            "\t if(uploadcount==uploadlimit){\n",
            "\t\talert('limit 1 file');\n"
            "\t\treturn false;\n"
            "\t }\n"
            
            "\t     for (var i = 0; i < files.length; i++) {\n",
            "\t\t       var file = files[i];\n",                    
            "\t\t       if(file.name){\n",
            "\t\t\t         var reader = new FileReader();",
            "\t\t\t         reader.index = uploadcount;",
            "\t\t\t         reader.file = file;",
            "\t\t\t         console.log(reader.file);",
            "\t\t\t         reader.currentFileIndex=i;",
            "\t\t\t         reader.addEventListener('loadend', handleFile, false);"
            "\t\t\t         reader.addEventListener('error', function(event){console.log('error '+event.code);}, false);\n\n",
            

            #"\t\t\t            reader.readAsBinaryString(file);",
            "\t\t\t         reader.readAsDataURL(file);",
                    
            "\t\t       };\n",
            "\t\t       uploadcount++;\n\n",    
            "\t     };\n",
            "}\n",
            
            "$(document).ready(function(){\n",
            "\t     $('.upload')[0].addEventListener('dragover', function(event){event.preventDefault();}, false);\n",
            "\t     $('.upload')[0].addEventListener('drop', upload, false);\n",
            "});")
            
        return self.javascript_html5fileHandle(id)+"\n".join(js)
        
    def get_value(self,name,value):
        count=0
        enum_name=name
        results=[' ',]
        #print name 
        #print value
        #while enum_name in value:
        #   print value.get(enum_name,'')
        #   print results
        #   results.append(value.get(enum_name,''))
        #   
        #   enum_name=name+str(count)
        #   count+=1
        return results

    #multiple plain text or numerical data form input
    def render(self):
        if self.mode==5:
            return self.html5()
        else:
            return self.html5()
                
        #plain text or numeric data
    def filepicker(self, name, values, error=0):  
        self.values = values
        title,value=self.form_node(self.values) 
        length=self.form_check_node(self.values,"length","")
        value=self.form_check_node(self.values,"self.values","")[0]

        if value=="":
            value=self.form_check_node(self.values,"default","")
        error_msg,style=self.form_error_notify(error)
        return self.form_node_wrap("<input type=\"file\" class=\"formtext\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\" maxlength=\""+str(length)+"\" value=\""+str(value)+"\" />",name,title,null=True,msg=error_msg)



    def html4(self):        
        title,value=self.form_node(self.values) 
        length=self.form_check_node(self.values,"length","")
        value=self.form_check_node(self.values,"self.values","")
        val=self.form_check_node(self.values,"val","t*")
        enum=self.form_check_node(self.values,"enum",0)
        seperator=self.form_check_node(self.values,"sep",None)

        if value==None:
            value=[self.form_check_node(self.values,"default","")]
        if value=="":
            value=[self.form_check_node(self.values,"default","")]
        if len(value)==0:
            value=[self.form_check_node(self.values,"default","")]        

        enum=len(value)
            
        error_msg,style=self.form_error_notify(error)
        
        if seperator:
            imgenum="<img src=\"/images/icons/silk/icons/add.png\" onclick=\"enum_textbox('"+name+"',"+str(enum)+");\"/>"+str(enum)+name
        else:
            imgenum=""
        form="<div id=\"cont_"+name+"\" class=\"form_entry_contain\">"
        val=""
        form+=self.form_node_wrap("<input type=\"file\" usm:valformat=\""+val+"\" class=\"formtext\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\" maxlength=\""+str(length)+"\" value=\""+str(value[0])+"\" />"+imgenum,name,title,null=True,msg=error_msg)

        for num in range(1,int(enum)):
            newname=name+str(num)
            #form+=self.form_node_wrap("<input class=\"formtext\" st yle=\""+style+"\" id=\""+newname+"\" name=\""+newname+"\" maxlength=\""+str(length)+"\" value=\""+str(value)+"\" />"+imgenum,newname,str(num)+title,null=True,msg=error_msg)
            form+=self.form_node_wrap("<input type=\"file\" usm:valformat=\""+val+"\" class=\"formtext\" style=\""+style+"\" id=\""+newname+"\" name=\""+newname+"\" maxlength=\""+str(length)+"\" value=\""+str(value[num])+"\" />"+imgenum,newname,"",null=True,msg=error_msg)
        form+="</div>"
        return self.form_node_contain(name,form)


    def html5(self):
        title,value=self.form_node(self.values) 
        length=self.form_check_node(self.values,"length","")
        value=self.form_check_node(self.values,"values","")
        val=self.form_check_node(self.values,"val","t*")
        enum=self.form_check_node(self.values,"enum",0)
        seperator=self.form_check_node(self.values,"sep",None)
        error_msg,style=self.form_error_notify(self.error)
        htm="<div class=\"upload\" id=\"%s\" >%s</div>" % (self.name, self.custom_message)
        form=self.form_fake_node_wrap("".join(htm),self.name,title,null=True,msg=error_msg)
        return self.form_node_contain(self.name,form)
        
        
