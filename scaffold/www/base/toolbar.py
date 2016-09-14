from ...core.widget import base_widget


class control(base_widget):  
    toolbar_class="toolbar"
    toolbar_title="default title"
    name="toolbarinfo"
    list=[]
    def javascript(self):
        js=("$(document).ready(function(){",
            "$('."+self.toolbar_class+" > .iconlink').bind('mouseout',this.hide());",
            "})")
        return "\n".join(js)
        
    #multiple plain text or numerical data form input
    def xhtmlbody(self,text,start="<br />",end=""):
    #def notifybox(self, text,start="<br />",end=""):
        return "%s<div class=\"amber\">%s</div>%s" % (start,text,end)
    
    def append(self,link,img,helptxt,name="toolbarinfo"):
        htm="<a class=\"iconlink\" href=\""+link+"\" onmouseout=\"document.getElementById(\'"+name+"\').style.display = \'none\';\" onmouseover=\"show_txt(\'"+name+"\',\'"+helptxt.replace("<","&lt;").replace(">","&gt;")+"\');\">"
        htm+="<img alt=\"icon\" class=\"icon\" src=\"%s\" /></a>" % (img)
        self.list.append(htm)

    #def tool_bar(self,title,icons,name="toolbarinfo",cssbar="toolbar",csstitle="toolbartitle",cssdesc="iconinfobar",cssicons="toolbaricons"):
    #   htm="\n<div class=\"%s\"><div class=\"%s\">%s</div><div class=\"toolbaricons\">%s</div>" % (cssbar,csstitle,title,icons)
    #   htm+="<div class=\"%s\" id=\"%s\"  >&#160;</div></div>\n<br />"% (cssdesc,name)
    #   return htm
                
    def tool_icon(self,link,img,help,name="toolbarinfo"):
        htm="<a class=\"iconlink\" href=\""+link+"\" onmouseout=\"document.getElementById(\'"+name+"\').style.display = \'none\';\" onmouseover=\"show_txt(\'"+name+"\',\'"+help.replace("<","&lt;").replace(">","&gt;")+"\');\">"
        htm+="<img alt=\"icon\" class=\"icon\" src=\"%s\" /></a>" % (img)
        return htm


    #def tool_bar(self,title,icons,name="toolbarinfo",cssbar="toolbar",csstitle="toolbartitle",cssdesc="iconinfobar",cssicons="toolbaricons"):
    #   htm="\n<div class=\"%s\"><div class=\"%s\">%s</div><div class=\"toolbaricons\">%s</div>" % (cssbar,csstitle,title,icons)
    #   htm+="<div class=\"%s\" id=\"%s\"  >&#160;</div></div>\n<br />"% (cssdesc,name)
    #   return htm
    #           
    #def tool_icon(self,link,img,help,name="toolbarinfo"):
    #   htm="<a class=\"iconlink\" href=\""+link+"\" onmouseout=\"document.getElementById(\'"+name+"\').style.display = \'none\';\" onmouseover=\"show_txt(\'"+name+"\',\'"+help.replace("<","&lt;").replace(">","&gt;")+"\');\">"
    #   htm+="<img alt=\"icon\" class=\"icon\" src=\"%s\" /></a>" % (img)
    #   return htm

    def title(self,toolbartitle):
        self.list=[]
        self.toolbar_title=toolbartitle

    def render(self):
        self.count+=1
        htm=(   "<div class=\"%s\">" % self.toolbar_class,
                "<div class=\"toolbartitle\">%s</div>" % self.toolbar_title,
                "<div class=\"toolbaricons\">%s</div>" % "".join(self.list),
                "<div class=\"iconinfobar\" id=\"%s\"  >&#160;</div>"% self.name,
                "</div>",
                "\n<br />",)
                
        return "\n".join(htm)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
