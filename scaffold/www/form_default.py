import os,sys
from . import forms 

class controls(object, forms.default.html_form_ui):
    includes=[]
    includes.append('<script type="text/javascript" src="/themes/web/js/lib_validate.js />')
    includes.append('<script type="text/javascript" src="/themes/web/js/lib_jquery_validate.js" />')
    includes.append('<script type="text/javascript" src="/themes/web/js/editor/editor.js" />')
    page_path=[]#url path page / subpage / action etc
    javascript={}
    htmlheader={}
    htmlfoot=""
    htmlbody=""
    form_count=0
    form_val={}
    map=forms.map.control()
    textbox=forms.textbox.control()
    textarea=forms.textarea.control()
    textedit=forms.texteditor.control()
    password=forms.password.control()
    locked=forms.locked.control()
    image=forms.image.control()
    ipv4=forms.ipv4.control()
    ipv6=forms.ipv6.control()
    upload=forms.upload.control()
    tags=forms.tags.control()
    listbox=forms.listbox.control()

    def create(self):
        pass

    def __init__(self):
        self.javascript={}
        self.htmlhead=""
        self.htmlfoot=""
        self.htmlbody=""
        
        self.form_val["textbox"]=forms.textbox.control(),("type")
        self.form_val["hidden"]=forms.hidden.control(),("type")
        self.form_val["mac"]=forms.mac.control(),("type")
        self.form_val["ipv4"]=forms.ipv4.control(),("type") 
        self.form_val["ipv6"]=forms.ipv6.control(),("type")
        self.form_val["textarea"]=forms.textarea.control(),("type")
        self.form_val["textedit"]=forms.texteditor.control(),("type")
        self.form_val["image"]=forms.image.control(),("type")
        self.form_val["tags"]=forms.tags.control(),("type")
        self.form_val["listbox"]=forms.listbox.control(),("type")
        self.form_val["checkbox"]=forms.checkbox.control(),("type")
        #self.form_val["textbox_enum"]=self.textbox,("type")
        #self.form_val["tickbox"]=self.tickbox,("type")
        #self.form_val["textarea"]=self.textarea,("type")
        #self.form_val["hidden"]=self.hidden,("type")
        self.form_val["locked"]=forms.locked.control(),("type")
        self.form_val["password"]=forms.password.control(),("type","values")
        self.form_val["subform"]=self.subform,('type','subformlist')
        #self.form_val["changepassword"]=self.changepassword,("type","values")
        #self.form_val["listbox"]=self.listbox,("type","values")
        #self.form_val["filelist"]=self.filelist,("type","values")
        self.form_val["dropdown"]=forms.combobox.control(),("type","values")
        #self.form_val["dropdown_enum"]=self.dropdown,("type","values")
        self.form_val["combobox"]=forms.combobox.control(),("type","values")
        self.form_val["upload"]=forms.upload.control(),("type","values")
        ##self.form_val["combobox_enum"]=self.combobox_enum,("type","values")
        #self.form_val["datebox"]=self.datebox,("type","values")
        #self.form_val["mac"]=self.mac,("type","values")
        #self.form_val["ipv4"]=self.ipv4,("type","values")
        #self.form_val["ipv6"]=self.ipv6,("type","values")
        #self.form_val["file"]=self.filepicker,("type","values")
        #self.form_val["chaincombobox"]=self.chaincombobox,("type","values","child")
        self.form_val["map"]=forms.map.control(),("type")

        self.form_error_msgs=[]
        self.form_error_msgs.append(("","border:2px solid #00ff00;"))
        self.form_error_msgs.append(("Added Extra Characters","border:2px solid #ff9000;"))
        self.form_error_msgs.append(("Invalid Characters Stripped Out","border:2px solid #ff9000;"))
        self.form_error_msgs.append(("Stopped At Invalid Character","border:2px solid #ff9000;"))  
        self.form_error_msgs.append(("This Field Requires A Value","border:2px solid #ff9000;"))   
        self.form_error_msgs.append(("Invalid format Entered, or required Field is blank","border:2px solid #ff0000;")) 
        #self.register()

    #default option
    def __getattr__(self,name):
        if name in self.elements:
            return self.elements[name]
        else:
            raise AttributeError(name)

    
    def render(self):
        result = {}
        result['htmbody'] = self.htmlbody
        result['jscript'] = ''
        for j in self.javascript.keys():
            result['jscript']+=self.javascript[j]
        return result

