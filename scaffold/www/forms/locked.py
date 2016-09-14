#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui

class control(html_form_ui):        
    def javascript(self,id=None):
        return ""

    def get_value(self,name,value):
        return [value[name]]  

    #multiple plain text or numerical data form input
    def render(self,name, dict, error=0):
        title,value=self.form_node(dict) 
        value=self.form_check_node(dict,"values","")[0]
        error_msg,style=self.form_error_notify(error)
        return self.form_node_wrap("<input class=\"formtext\" readonly=\"readonly\" name=\""+name+"\" id=\""+name+"\" value=\""+value+"\" />",name,title,error_msg)


    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
