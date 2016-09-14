#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui

class control(html_form_ui):        
    def javascript(self,id=None):
        js=("function enum_textbox(name,start){\n",
            "\tif(form_enum[name]===0){\n",
            "\t\tform_enum[name]=start;\n",
            "\t}\n",
                
            "\tif(form_enum[name]===undefined){\n",
            "\t\tform_enum[name]=0;\n",
            "\t}else{\n",
            "\t\tform_enum[name]++;\n",
            "\t}\n",
            
            "\tvar frmname=name+form_enum[name].toString();",
            
            "\tvar item = document.getElementById('cont_'+name);\n",
            "\tvar newitem =  document.createElement(\"input\");\n",
            "\tvar newlabel =  document.createElement(\"label\");\n",
            "\tnewlabel.setAttribute(\"for\",frmname);\n",
            
            "\tnewitem.setAttribute(\"name\",frmname);\n",
            "\tnewitem.setAttribute(\"id\",frmname);\n",
            "\tnewitem.setAttribute(\"class\",'formtext');\n",
            
            "\titem.appendChild(newlabel);\n",
            "\titem.appendChild(newitem);\n",
            
            "}\n",)
        return "\n".join(js)

    def get_value(self,name,value):
        result=value[name+'1'][0]+':'+value[name+'2'][0]+':'+value[name+'3'][0]+':'+value[name+'4'][0]
        result+=':'+value[name+'5'][0]+':'+value[name+'6'][0]+':'+value[name+'7'][0]+':'+value[name+'8'][0]
        return [result]  
 

    #multiple plain text or numerical data form input
    def render(self,name, dict, error=0):
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
            imagenum="<img src=\"/images/icons/silk/icons/add.png\" onclick=\"enum_textbox('"+name+"',"+str(enum)+");\"/>"+str(enum)+name
        else:
            imagenum=""
        form="<div id=\"cont_"+name+"\" class=\"form_entry_contain\">"
        val=""

        title,value=self.form_node(dict) 
        ipvalue=self.form_check_node(dict,"values","")[0].split(".")
        
        
        form+=self.form_node_wrap(self.html5body(name,ipvalue)+imagenum,name,title,msg=error_msg)

        #formip+="</div>"
        error_msg,style=self.form_error_notify(error)



        for num in range(1,int(enum)):
            newname=name+str(num)
            #form+=self.form_node_wrap("<input class=\"formtext\" st yle=\""+style+"\" id=\""+newname+"\" name=\""+newname+"\" maxlength=\""+str(length)+"\" value=\""+str(value)+"\" />"+imgenum,newname,str(num)+title,null=True,msg=error_msg)
            title,value=self.form_node(dict) 
            ipvalue=self.form_check_node(dict,"values","")[0].split(".")
            form+=self.form_node_wrap(self.html5body(name,ipvalue)+imagenum,name,title,null=True,msg=error_msg)
        form+="</div>"
        return self.form_node_contain(name,form)


    def xhtmlhead(self):
        return ""

    def html5body(self,name,ipvalue):
        try:
            htm=("<div class=\"ipcont\">",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"1\" value=\""+ipvalue[0]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"2\" value=\""+ipvalue[1]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"3\" value=\""+ipvalue[2]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"4\" value=\""+ipvalue[3]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"5\" value=\""+ipvalue[4]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"6\" value=\""+ipvalue[5]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"7\" value=\""+ipvalue[6]+"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"8\" value=\""+ipvalue[7]+"\" maxlength=\"4\" />",
            "</div>")
        except:
            htm=("<div class=\"ipcont\">",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"1\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"2\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"3\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"4\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"5\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"6\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"7\" value=\"\" maxlength=\"4\" />",
            "<input type=\"text\" class=\"ipv6\" name=\""+name+"8\" value=\"\" maxlength=\"4\" />",
            "</div>")
        return "\n".join(htm)

    def html5head(self):
        return ""
