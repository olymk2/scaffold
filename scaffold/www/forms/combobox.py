from .default import html_form_ui

class control(html_form_ui):        
    def js_enum(self):
        js=("function enum_combobox(name,start){",
        "\tif(form_enum[name]===0){",
        "\t\tform_enum[name]=start;",
        "\t}",
        "\tif(form_enum[name]===undefined){",
        "\t\tform_enum[name]=0;",
        "\t}else{\n",
        "\t\tform_enum[name]++;",
        "\t}",
        "\tvar frmname=name+form_enum[name].toString();",

        "\tvar item = document.getElementById(name);",
        "\tvar newitem = document.getElementById(name).cloneNode(true);",
        "\tvar newlabel =  document.createElement(\"label\");",
        "\tnewlabel.setAttribute(\"for\",frmname);",
        "\tnewitem.setAttribute(\"name\",frmname);",
        "\tnewitem.setAttribute(\"id\",frmname);",
        "\titem.parentNode.appendChild(newlabel);",
        "\titem.parentNode.appendChild(newitem);",
        "}",)
        return "\n".join(js)
    
    def javascript(self,id=None):
        return self.js_enum()
    
    def render(self,name, dict, error=0):
        return self.xhtmlbody(name, dict, error)
    
    #multiple plain text or numerical data form input
    def xhtmlbody(self,name, dict, error=0):
        title,value=self.form_node(dict) 
        values=self.form_check_node(dict,"values","")
        defaultlist=self.form_check_node(dict,"options","")
        enum=self.form_check_node(dict,"enum",None)
        seperator=self.form_check_node(dict,"sep",0)
        
        formout=""
        formname=name
        combovalue=""
        comboname=""
        if enum:
            count=len(values)
        else:
            count=1
        form=""
        for num in range(0,int(count)):
            form+="<select id=\""+formname+"\" name=\""+formname+"\">"
            if seperator!="" and seperator!=None:
                for item in defaultlist.split(seperator*2):
                    try:
                        combovalue,comboname=item.split(seperator)
                    except:
                        comboname=item
                        combovalue=item   
                    if item!="":
                        if combovalue==values[num]:
                            form+="<option selected=\"selected\" value=\""+combovalue+"\">"+comboname.replace("&","&amp;")+"</option>"             
                        else:
                            form+="<option value=\""+combovalue+"\">"+comboname.replace("&","&amp;")+"</option>"
      
            else:
                for item in defaultlist.split("||"):
                    try:
                        combovalue,comboname=item.split("|")
                    except:
                        comboname=item
                        combovalue=item
                    if item!="":
                        if combovalue==values[num]:
                            form+="<option selected=\"selected\" value=\""+combovalue+"\">"+comboname.replace("&","&amp;")+"</option>"             
                        else:
                            form+="<option value=\""+combovalue+"\">"+comboname.replace("&","&amp;")+"</option>"
            form+="</select>"
            if enum:
                form+="<img src=\"/images/icons/silk/icons/add.png\" onclick=\"enum_combobox('"+name+"',"+str(enum)+");\"/>"+str(enum)+name
            else:
                formname=name+str(num)
            error_msg,style=self.form_error_notify(error)
            formout+=self.form_node_labels(form,formname,title,msg=error_msg)
        return self.form_node_contain(name,formout)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
