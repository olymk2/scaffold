from .default import html_form_ui

class control(html_form_ui):        
    def javascript(self,id=None):
        js=("",)
        return "\n".join(js)

    def get_value(self,name,value):
        result=value[name+'1'][0]+':'+value[name+'2'][0]+':'+value[name+'3'][0]+':'+value[name+'4'][0]
        result+=':'+value[name+'5'][0]+':'+value[name+'6'][0]
        return [result]  
 
    def render(self, name, dict, error=0):
        title,value=self.form_node(dict) 
        macvalue=self.form_check_node(dict,"values","")[0].split(".")
        try:
            formmac="<div class=\"maccont\">"
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"1\" value=\""+macvalue[0]+"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"2\" value=\""+macvalue[1]+"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"3\" value=\""+macvalue[2]+"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"4\" value=\""+macvalue[3]+"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"5\" value=\""+macvalue[4]+"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"6\" value=\""+macvalue[5]+"\" />";
        except:
            formmac="<div class=\"maccont\">"
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"1\" value=\"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"2\" value=\"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"3\" value=\"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"4\" value=\"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"5\" value=\"\" />";
            formmac+="<input type=\"text\" class=\"mac\" maxlength=\"2\" name=\""+name+"6\" value=\"\" />";
        formmac+="</div>"
        error_msg,style=self.form_error_notify(error)
        return self.form_node_wrap(formmac,name,title,msg=error_msg)

    def html5head(self):
        return ""
