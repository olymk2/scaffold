from .default import html_form_ui

class control(html_form_ui):
    def js_enum(self):
        js=("function insertOption(elem,value){\n",
            "\tvar elSel = document.getElementById(elem);\n",
            "\t\tvar option=new Option(value,value);\n",
            "\t\telSel.options.add(option);\n",
            "}\n",
            
            "function insertOptionArray(elem,value){\n",
            "\tvar elSel = document.getElementById(elem);\n",
            "\tfor (var i=0;i<chaincombo[value].length;i++){\n",
            "\t\tvar option=new Option(chaincombo[value][i][1],chaincombo[value][i][0]);\n",
            "\t\telSel.options.add(option);\n",
            "\t};\n",
            "}\n",
            
            "function removeOptionSelected(elem){\n",
            "\tvar elSel = document.getElementById(elem);\n",
            "\tfor(var i = elSel.length - 1; i>=0; i--) {\n",
            "\t\tif(elSel.options[i].selected) {\n",
            "\t\t\telSel.remove(i);\n",
            "\t\t}\n",
            "\t}\n",
            "}\n",
            
            "function removeOptionAll(elem){\n",
            "\tvar elSel = document.getElementById(elem);\n",
            "\telSel.options.length=0;\n",
            "}\n")
        return "\n".join(js)
    
    def javascript(self,id=None):
        return self.js_enum()
    
    def render(self,name, dict, error=0):
        return self.xhtmlbody(name, dict, error)
    
    #multiple plain text or numerical data form input
    def xhtmlbody(self,name, dict, error=0):
        title,value=self.form_node(dict) 
        value=self.form_check_node(dict,"values","")[0]
        results=self.form_check_node(dict,"options","")
        error_msg,style=self.form_error_notify(error)
        options={}
        if results is not None:
            options=results.split(",")
        
        multi=""
        multiarea=""
        form=""
        clist=""
        for item in options:
            clist+="<option value=\""+item+"\">"+item+"</option>"
 
        for item in value.split(","):
            multi+="<option selected=\"selected\" value=\""+item+"\">"+item+"</option>"
            multiarea+=item+"\n"

        form+="<select  name=\""+name+"\" id=\""+name+"\" readonly=\"readonly\" multiple=\"multiple\" size=\"10\"  >"+multi+"</select>"
        form+="<br /><label for=\"a"+name+"\">Add to "+title+"&#160;:&#160;</label><select onchange=\"insertOption('s"+name+"',this.options[this.selectedIndex].value);\" name=\"a"+name+"\">"+clist+"</select>"#</div>"
        form+="<br /><label for=\"r"+name+"\">Remove From "+title+"&#160;:&#160;</label><input name=\"r"+name+"\" type=\"button\" value=\"Remove Seleted\" onclick=\"removeOptionSelected('s"+name+"');returnlist('s"+name+"','"+name+"');\" />"
        formout=self.form_node_labels(form,name,title,msg=error_msg)
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
