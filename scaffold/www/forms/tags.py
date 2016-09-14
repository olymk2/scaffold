#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui
import sys
class control(html_form_ui):        
    def javascript(self,id=None):
        
        js=("$(document).ready(function(){",
                "$('.keywords').each(function(){", #enum_textbox(name,start){\n",
                    "var current=this;",
                    "$('#%s_entry',this).keypress(function(e){"%id,
                        "if( e.which==32){",
                            "txt='<div class=\"tag\"><div class=\"word\">'+$('#%s_entry').val()+'</div>';" %id,
                            "txt+='<div class=\"arrow\"></div></div>';",
                            "$(current).append(txt);",
                            "$(\'input:first\',current).val($(\'.keywords input:first\').val()+$(this).val());",
                            "$(this).val('');",
                        "}",
                    "})",
                    
                    "$('.arrow',this).click(function(e){",
                        "alert('remove word to come');",
                    "})",
                    
                "})",
            "})\n",)
        return "\n".join(js)

    def tag(self,word):
        txt='<div class="tag"><div class="word">'+str(word)+'</div>'
        txt+='<div class=\"arrow\"></div></div>'
        return txt
        

    def get_value(self,name,value):
        result=value.get(name,'')
        if result:
            result=result[0].split()
        return [result]

    #multiple plain text or numerical data form input
    def render(self,name, dict, error=None):
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
        form= "<div class=\"keywords\">"
        form+="<div style=\"clear:both;\"></div>"
        form+="<input type=\"hidden\" usm:valformat=\""+val+"\" class=\"formhide\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\" maxlength=\""+str(length)+"\" value=\""+' '.join(value)+"\" />"
        form+="<input usm:valformat=\""+val+"\" class=\"formtags\" style=\""+style+"\" id=\""+name+"_entry\" name=\""+name+"\" maxlength=\""+str(length)+"\" value=\"\" />"+imgenum
        form+="<div id=\"cont_"+name+"\" class=\"form_entry_contain\">"
        val=""
        for v in value:
            for word in v.split(' '):
                if word!='': 
                    form+='t'+self.tag(word)    
        form+='</div></div>'        
        form=self.form_node_wrap(form,name,title,null=True,msg=error_msg)



        return self.form_node_contain(name,form)

    def xhtmlhead(self):
        return ""

    def html5head(self):
        return ""
