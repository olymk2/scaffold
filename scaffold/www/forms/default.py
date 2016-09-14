import sys

class html_form_ui:
    jscript=False
    mode=0#0=html4, 1=html5
    showerrors=1
    javascript=''
    tab=0
    node_wrap=False
    count=0

    form_error_msgs=[]
    form_error_msgs.append(("",""))#0
    form_error_msgs.append(("","border:2px solid #00ff00;"))#1
    form_error_msgs.append(("Added Extra Characters","border:2px solid #ff9000;"))#2
    form_error_msgs.append(("Invalid Characters Stripped Out","border:2px solid #ff9000;"))#3
    form_error_msgs.append(("Stopped At Invalid Character","border:2px solid #ff9000;"))#4
    form_error_msgs.append(("This Field Requires A Value","border:2px solid #ff9000;"))#5   
    form_error_msgs.append(("Invalid format Entered, or required Field is blank","border:2px solid #ff0000;"))#6
    
    plugin=""
    html=[]
    def get_value(self,name,value):
        return [value.get(name,None),]  
          
    def javascript(self,id=None):
        pass
    
    
    
    #def html(self):
    #   pass
    #   
    #def xhtmlbody(self):
    #   pass

    #def xhtmlhead(self):
    #   pass

    #def html5body(self):
    #   pass

    #def html5head(self):
    #   pass



    #get form fields title and default value
    def form_node(self,dict):#get value and title
        if "friendly" in dict:
            title=dict["friendly"]
        else:
            title=""
        if 'values' in dict:
            value=dict["values"]
        else:
            value=None
        return title,value

    def form_check_node(self,dict,node,value=""):
        if node=="values":
            if node in dict.keys():
                if dict[node] is not None:
                    return dict[node]
                else:
                    return ['']
            else:
                return ['']
        else:
            if node in dict.keys():
                return dict[node]
            else:
                return None
    
    #Find error msg info to display above form nodes
    def form_error_notify(self,error=None):
        msg=""
        warn=""
        if self.showerrors==1 and error!=None:
            #sys.exit(0)
            msg,warn=self.form_error_msgs[error]
            if error==0:
                msg,warn=self.form_error_msgs[error]
        return msg,warn
        
    #wrap the form fields in this code, used for highlighting error and displaying labels
    def form_node_wrap(self,item,name="",title="",null=False,msg=""):
        form="<div id=\"frm_%s\">\n" % name 
        self.tab+=1
        if msg!="":
            form+="<b>"+msg+"</b><br />"
            
        if title!="":
            if null==True:
                form+="<label for=\""+name+"\">*&#160;"+title+"&#160;:&#160;</label>"+item+"<br />"
            else:
                form+="<label for=\""+name+"\">&#160;"+title+"&#160;:&#160;</label>"+item+"<br />"
        else:
            form+="<label for=\""+name+"\">*&#160;&#160;:&#160;</label>"+item+"<br />"
        self.tab-=1
        return form+"\n</div>\n" 

    #wrap the form fields in this code, used for highlighting error and displaying labels
    def form_fake_node_wrap(self,item,name="",title="",null=False,msg=""):
        form="<div id=\"frm_%s\">\n" % name 
        self.tab+=1
        if msg!="":
            form+="<b>"+msg+"</b><br />"
            
        if title!="":
            if null==True:
                form+="<div class=\"fakelabel\">*&#160;"+title+"&#160;:&#160;</div>"+item+"<br />"
            else:
                form+="<div class=\"fakelabel\">&#160;"+title+"&#160;:&#160;</div>"+item+"<br />"
        else:
            form+="<div>*&#160;&#160;:&#160;</div>"+item+"<br />"
        self.tab-=1
        return form+"\n</div>\n" 

    def form_node_contain(self,name,text):
        return '<div id="cont'+name+'" class="form_node_contain">\n%s<div style="clear:both;"></div></div>\n' % text

    def form_node_labels(self,item,name="",title="",null=False,msg=""):
        form=""
        self.tab+=1
        if msg!="":
            form+="<b>"+msg+"</b><br />"
            
        if title!="":
            if null==True:
                form+="<label for=\""+name+"\">*&#160;"+title+"&#160;:&#160;</label>"+item+"<br />"
            else:
                form+="<label for=\""+name+"\">&#160;"+title+"&#160;:&#160;</label>"+item+"<br />"
        else:
            form+="<label for=\""+name+"\">*&#160;&#160;:&#160;</label>"+item+"<br />"
        self.tab-=1
        return form

    def render(self):
        return "/n".join(self.html)
