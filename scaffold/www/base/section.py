from ...core.widget import base_widget


class control(base_widget):  
    slideable=True
    hidden=True
    list=[]
    htmtitle=''
    htminfo=None
    htmbody=''
    htmfooter=[]
    js={}
    def javascript(self):
        
        
        js=("$(document).ready(function(){\n",
            "\t$('.sectionexpand').click(function(){\n",
            "\t\t$(this).next().toggle(400);\n",
            "\t});\n",
            "});\n")
            
        self.js['expandable']="\n".join(js)
        return "\n".join(js)
    
    def reset(self):
        self.htmtitle=''
        self.htmbody=''
        self.htmfooter=[]
     
    #multiple plain text or numerical data form input
    def xhtmlbody(self,text,start="<br />",end=""):
    #def notifybox(self, text,start="<br />",end=""):
        return "%s<div class=\"amber\">%s</div>%s" % (start,text,end)
    
    def append(self,htm):
        self.list.append(htm)

    def title(self,htm):
        self.htmtitle=htm

    def info(self,htm):
        self.htminfo=htm

    def body(self,htm):
        self.htmbody=htm

    def content(self,htm):
        self.htmbody=htm

    def footer(self,htm):
        self.htmfooter.append("%s" % htm)

    def render(self,id="notify",htm=""):
        self.count+=1
        htm=(   "<div class=\"sectioncont\">",
                "<div class=\"sectiontitle\"><h2>%s</h2></div>"% self.htmtitle,
                "<div class=\"sectioninfo\">%s</div>"% self.htminfo,
                "<div class=\"sectionbody\">%s</div>"% self.htmbody,
                "<div class=\"sectionexpand\">expand</div>",
                "<div class=\"sectionfooter\">%s</div>" % "".join(self.htmfooter),
                
                "</div>",)
        self.reset()
        return "\n".join(htm)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" class=\"section\"\">",
        
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""

    def traffic_lights(self,col,title,text):
        htm="<br /><br /><br /><div onload=\"swapDivs('traffic');\" id=\"traffic\" class=\""+col+"\"><font class=\"traffichead\">"+title+"</font><br />"+text+"</div>"
        return htm
         

