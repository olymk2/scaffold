#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui
import sys
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
        value=[value[name+'1'][0]+'.'+value[name+'2'][0]+'.'+value[name+'3'][0]+'.'+value[name+'4'][0]]
        return  [value]

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
            imgenum="<img src=\"/images/icons/silk/icons/add.png\" onclick=\"enum_textbox('"+name+"',"+str(enum)+");\"/>"+str(enum)+name
        else:
            imgenum=""
        form="<div id=\"cont_"+name+"\" class=\"form_entry_contain\">"
        val=""

        title,value=self.form_node(dict) 
        ipvalue=self.form_check_node(dict,"values","")[0].split(".")
        try:
            #formip="<div class=\"ipcont\">"
            formip="<input usm:valformat=\""+val+"\" type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"1\" name=\""+name+"1\" value=\""+ipvalue[0]+"\" maxlength=\"3\" />";
            formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"2\" name=\""+name+"2\" value=\""+ipvalue[1]+"\" maxlength=\"3\" />";
            formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"3\" name=\""+name+"3\" value=\""+ipvalue[2]+"\" maxlength=\"3\" />";
            formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"4\" name=\""+name+"4\" value=\""+ipvalue[3]+"\" maxlength=\"3\" />";
            
        except:
            #formip="<div class=\"ipcont\">"
            formip="<input ctype=\"text\" lass=\"ipv4\" id=\""+name+"1\" name=\""+name+"1\" value=\"\" maxlength=\"3\" />";
            formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"2\" name=\""+name+"2\" value=\"\" maxlength=\"3\" />";
            formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"3\" name=\""+name+"3\" value=\"\" maxlength=\"3\" />";
            formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"4\" name=\""+name+"4\" value=\"\" maxlength=\"3\" />";
        
        form+=self.form_node_wrap(formip+imgenum,name,title,null=True,msg=error_msg)
        #formip+="</div>"
        error_msg,style=self.form_error_notify(error)



        for num in range(1,int(enum)):
            newname=name+str(num)
            #form+=self.form_node_wrap("<input class=\"formtext\" st yle=\""+style+"\" id=\""+newname+"\" name=\""+newname+"\" maxlength=\""+str(length)+"\" value=\""+str(value)+"\" />"+imgenum,newname,str(num)+title,null=True,msg=error_msg)
            title,value=self.form_node(dict) 
            ipvalue=self.form_check_node(dict,"values","")[0].split(".")
            try:
                #formip="<div class=\"ipcont\">"
                formip="<input usm:valformat=\""+val+"\" type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"1\" name=\""+name+"1\" value=\""+ipvalue[0]+"\" maxlength=\"3\" />";
                formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"2\" name=\""+name+"2\" value=\""+ipvalue[1]+"\" maxlength=\"3\" />";
                formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"3\" name=\""+name+"3\" value=\""+ipvalue[2]+"\" maxlength=\"3\" />";
                formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"4\" name=\""+name+"4\" value=\""+ipvalue[3]+"\" maxlength=\"3\" />";
            except:
                #formip="<div class=\"ipcont\">"
                formip="<input ctype=\"text\" lass=\"ipv4\" id=\""+name+"1\" name=\""+name+"1\" value=\"\" maxlength=\"3\" />";
                formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"2\" name=\""+name+"2\" value=\"\" maxlength=\"3\" />";
                formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"3\" name=\""+name+"3\" value=\"\" maxlength=\"3\" />";
                formip+="<input type=\"text\" size=\"3\" class=\"ipv4\" id=\""+name+"4\" name=\""+name+"4\" value=\"\" maxlength=\"3\" />";
            form+=self.form_node_wrap(formip+imgenum,name,title,null=True,msg=error_msg)
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
