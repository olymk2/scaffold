#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui

class control(html_form_ui):        
    def javascript(self,id=None):
        js=(#"var form_enum={};\n"
            "function enum_textbox(name,start){\n",
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
        count=0
        enum_name=name
        results=[]
        #results.append(value.get(name,None))
        while enum_name in value:
            results.append(value.get(enum_name,None))
            
            enum_name=name+str(count)
            count+=1
        return results  

    #multiple plain text or numerical data form input
    def create(self,name, dict={}, error=None):
        self.html=[]
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
        form="<input sa:valformat=\""+val+"\" class=\"formtext\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\" maxlength=\""+str(length)+"\" value=\""+str(value[0])+"\" />"
        if self.node_wrap==True:
            self.html.append(self.form_node_contain(name,form))
        else:
            self.html.append(form)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
