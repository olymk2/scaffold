#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui

class control(html_form_ui):        
    def javascript(self,id=None):
        return ""

    #password filed, requires validation
    def render(self, name,dict,error=0):
        title,value=self.form_node(dict) 

        value=self.form_check_node(dict,"values","")
        val=self.form_check_node(dict,"val","p*")
        error_msg,style=self.form_error_notify(error)
        form=self.form_node_wrap("<input usm:valformat=\""+val+"\" type=\"password\" id=\""+name+"\"  name=\""+name+"\" />",name,"New "+title,error_msg)
        form+=self.form_node_wrap("<input usm:valformat=\""+val+"\" type=\"password\" id=\""+name+"confirm\"  name=\""+name+"confirm\" />",name,"Confirm "+title,"")
        return form

    def get_value(self,name,value):

        return [value.get(name,None)]  

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
