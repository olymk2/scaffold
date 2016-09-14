#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui

class control(html_form_ui):        
    count = 0
    #multiple plain text or numerical data form input
    #def create(self, name, value, label= '', attributes = []):
    def create(self, name, dict={}, error=0):
        self.html=[]
        title, value=self.form_node(dict) 
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
        return self

    def render(self):
        return '<label for=""></label><input %s >' % self.get_attributes()
