#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui

class control(html_form_ui):  

    def javascript(self,id=None):
        js=("",)
        return "\n".join(js)



    def get_value(self,name,value):
        #print name+"textarea get value="+str(value)
        #return [value.get(name,None)]  
        count=0
        enum_name=name
        results=[]
        #results.append(value.get(name,None))
        while enum_name in value:
            results.append(value.get(enum_name,None))
            
            enum_name=name+str(count)
            count+=1
        return results  
        
    #large amount of text
    def render(self, name, dict, error=0):
        title,value=self.form_node(dict) 
        value=self.form_check_node(dict,"values",'')
        
        if value==None:
            value=[self.form_check_node(dict,"default","")]
        if value=="":
            value=[self.form_check_node(dict,"default","")]
        if len(value)==0:
            value=[self.form_check_node(dict,"default","")] 
        error_msg,style=self.form_error_notify(error)
        return self.form_node_wrap("<textarea cols=\"50\" rows=\"5\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\">"+value[0]+"</textarea>",name,title,msg=error_msg);
        

    #multiple plain text or numerical data form input
    def renderold(self,name, dict, error=0):
        title,value=self.form_node(dict) 
        length=self.form_check_node(dict,"length","")
        value=self.form_check_node(dict,"values","")
        val=self.form_check_node(dict,"val","t*")
        enum=self.form_check_node(dict,"enum",0)
        seperator=self.form_check_node(dict,"sep",None)

        if value==None:
            value=[self.form_check_node(dict,"default","")]
        if value=="":
            value=[self.form_check_node(dict,"default","")]
        if len(value)==0:
            value=[self.form_check_node(dict,"default","")]        

        enum=len(value)
            
        error_msg,style=self.form_error_notify(error)
        
        if seperator:
            imgenum="<img src=\"/images/icons/silk/icons/add.png\" onclick=\"enum_textbox('"+name+"',"+str(enum)+");\"/>"+str(enum)+name
        else:
            imgenum=""
        form="<div id=\"cont_"+name+"\" class=\"form_entry_contain\">"
        val=""
        form+=self.form_node_wrap("<input usm:valformat=\""+val+"\" class=\"formtext\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\" maxlength=\""+str(length)+"\" value=\""+str(value[0])+"\" />"+imgenum,name,title,null=True,msg=error_msg)

        for num in range(1,int(enum)):
            newname=name+str(num)
            #form+=self.form_node_wrap("<input class=\"formtext\" st yle=\""+style+"\" id=\""+newname+"\" name=\""+newname+"\" maxlength=\""+str(length)+"\" value=\""+str(value)+"\" />"+imgenum,newname,str(num)+title,null=True,msg=error_msg)
            form+=self.form_node_wrap("<input usm:valformat=\""+val+"\" class=\"formtext\" style=\""+style+"\" id=\""+newname+"\" name=\""+newname+"\" maxlength=\""+str(length)+"\" value=\""+str(value[num])+"\" />"+imgenum,newname,"",null=True,msg=error_msg)
        form+="</div>"
        return self.form_node_contain(name,form)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
