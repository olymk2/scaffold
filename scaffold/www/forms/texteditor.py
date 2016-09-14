#from libs.v4.www.forms.default import html_form_ui
import sys
from .default import html_form_ui

class control(html_form_ui):
    escape_list={'<':'&lt;','>':'&gt;','&':'&amp;'}         
    def javascript(self,id=None):

        js=("\t$(document).ready(function(){",
        
        #"\t\t\t$('.texteditor .preview img').live('click',function(){",
        #"\t\t\talert('test');",
        #"\t\t\t\tinsertImage($(this).attr('src'));",
        ##"\t\t\t\tinsertAtCursor($('textarea')[0],$(this).attr('src'));",
        #"\t\t\t\t$('#vieweditor').hide();",
        #"\t\t\t});",
        
        "\t$('#vieweditor > .close').click(function(){",
        "\t\t$('#vieweditor').hide();",
        "\t})",
        "\t$('.selectImage').click(function(){",
        "\t$.ajax({",
        "\t\turl:'/ajax/blog/preview/',",
        "\t\ttype:'GET',",
        "\t\tdataType:'html',",
        "\t\tsuccess:function(data){",
        "\t\t\t$('#vieweditor > .insert').html(data);",
        "\t\t\t$('#vieweditor > .preview > img').live('click',function(){",
        "\t\t\talert('test');",
        #"\t\t\t\tinsertAtCursor($('#content')[0],$(this).attr('src'));",
        #"\t\t\t\tinsertImage($(this).attr('src'));",
        "\t\t\t\tapply($(this).attr('src'));",

        "\t\t\t\t$('#vieweditor').hide();",
        "\t\t\t});",
        "\t$('#vieweditor').show();",   
        #"\t\t\talert(data);",
        "\t\t},",
        "\t\terror:function(data,error){",
        "\t\t\tconsole.log(error);",
        "\t\t}",        
        "\t});",
        #"\talert('show images');",
        
        "\t});",
        self.javascript_preview(id),
        "});")
        jsstr=self.javascript_insert_at_cursor()
        jsstr+="\n".join(js)
        return jsstr

    def escape(self,text):
        """
        scan through text escaping special html characters
        """

        self.text=text
        self.textlen=len(text)-1
        self.result=""

        self.textpos=0
        while self.textpos<self.textlen:
            if self.text[self.textpos] in self.escape_list.keys():
                self.result+=self.escape_list[self.text[self.textpos]]
            else:
                self.result+=self.text[self.textpos]
            self.textpos+=1

        print(self.result)
        
        return self.result

    def javascript_include(self):
        return '<script type="text/javascript" src="web/js/editor.js" />'
        

    def javascript_preview(self,id):
        js=("$('.media').click(function(){",
                "$.ajax({",
                    "url:'/ajax/blog/preview/',",
                    "dataType:'html',",
                    "success:function(data){",
                        "\tconsole.log(data);",
                        "$('.preview .content').html(data);",
                        "$('.preview').show();",
                    "},",
                    "error:function(){",
                        "\talert('error='+data);",
                    "}",
                "});",
            "});")
        return "\n".join(js)

    def javascript_insert_at_cursor(self):
        js=("function insertAtCursor(element, text) {",
            "\t//IE support",
            "\tif (document.selection) {",
            "\t\telement.focus();",
            "\t\tsel = document.selection.createRange();",
            "\t\tsel.text = text;",
            "\t}",

            "\telse if (element.selectionStart || element.selectionStart == '0') {",
            "\tvar startPos = element.selectionStart;",
            "\tvar endPos = element.selectionEnd;",
            "\telement.value = element.value.substring(0, startPos)",
            "\t+ text",
            "\t+ element.value.substring(endPos, element.value.length);",
            "\t} else {",
            "\telement.value += text;",
            "\t}",
            "}")
        return "\n".join(js)
        

    def get_value(self,name,value):
        return [value.get(name,''),]  

    #multiple plain text or numerical data form
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
        #form+="<div class=\"selectImage\">Image</div><div class=\"selectVideo\">Video</div><div id=\"vieweditor\" style=\"z-index:1;position:absolute;top:0px;left:0px;bottom:0px;right:0px;margin:50px;background-color:#666666;display:none;\"><div class=\"close\">close</div><div class=\"insert\"></div></div>"
        #form+="<div class=\"preview\">Preview</div>"
        #form+=self.form_node_wrap("<div contentEditable=\"true\" style=\"width:100%;height:100px;\" id=\"edit_"+name+"\" name=\""+name+"\" >test text</div>"+imgenum,name,title,null=True,msg=error_msg)
        

        editor="""<div class="texteditor">
            <div class="edittools" style="position:relative;border:1px solid #000;">
                <div style="background-color:#D0D0D0;" class="title">
                <div style="float:left;width:100px;" class="btn format">Format</div>
                <div style="float:left;width:100px;" class="btn insert">Insert</div>
                <div style="float:left;width:100px;" class="btn media">Media</div>
                <div style="clear:both;"></div>
            </div>
            
            <div class="icons">
            <div class="btns">
                
                <div class="row1 bold"></div>
                <div class="row1 italic"></div>
                <div class="row1 underline"></div>
                
                <div class="row1 h1"></div>
                <div class="row1 h2"></div>
                <div class="row1 h3"></div>             
                
                <div class="row1 pre">pre</div>
                
                <div class="row2 btn4"></div>
                <div class="row2 btn5"></div>
                <div class="row2 p"></div>

                <div class="row2 h4"></div>
                <div class="row2 h5"></div>
                <div class="row2 h6"></div>
                
                <div style="clear:both;display:none;"></div>
            </div>
            
            </div>
            
        </div><div style="clear:both;"></div>"""
        

        editor+="""<div class="editcontent" contenteditable="true">
                <div id="content">"""+value[0]+"""</div>
            </div>
            <div id="editstatus" class="editstatus">n=<span class="editnode"></span>&nbsp;|&nbsp;s=<span class="editstart"></span>&nbsp;|&nbsp;e=<span class="editend"></span>&nbsp;|&nbsp;</div>"""

        editor+="<textarea usm:valformat=\""+val+"\" class=\"formtext\" style=\""+style+"\" id=\""+name+"\" name=\""+name+"\" >"+self.escape(str(value[0]))+"</textarea>"+imgenum
        editor+="<div class=\"preview\" style=\"z-index:6;width:600px;height:400px;display:none;\"><div class=\"title\">Please Select an image<div class=\"close\">X</div></div>"
        editor+="<div class=\"align\"><form><select name=\"position\"><option value=\"left\">Left</option><option value=\"middle\">Middle</option><option value=\"right\">Right</option></select><input type=\"text\" name=\"alt\"/></form></div>"
        editor+="<div class=\"content\"></div></div>"
        editor+="</div>"
        
        htm=(   "<div class=\"upload\" id=\"%s\" >" % name,
        "</div>")
        form=self.form_fake_node_wrap("".join(editor),name,title,null=True,msg=error_msg)
        #form+=self.form_node_wrap(editor,name,title,null=True,msg=error_msg)


        #form+="</div>"
        return self.form_node_contain(name,form)
        #return "\n".join(htm)

    

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        return ''
        
    def html5head(self):
        return ""
