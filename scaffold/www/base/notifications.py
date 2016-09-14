from ...core.widget import base_widget


class control(base_widget):  
    list=[]
    def javascript(self,id=None):
        js=("",)
        return "\n".join(js)
        
    #multiple plain text or numerical data form input
    def xhtmlbody(self,text,start="<br />",end=""):
    #def notifybox(self, text,start="<br />",end=""):
        return "%s<div class=\"amber\">%s</div>%s" % (start,text,end)
    
    def append(self,htm):
        self.list.append(htm)

    def render(self,id="notify",htm=""):
        self.count+=1
        return "<div id=\"%s%d\">%s</div>" %(id,self.count,"\n".join(self.list))

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""

    def traffic_lights(self,col,title,text):
        htm="<br /><br /><br /><div onload=\"swapDivs('traffic');\" id=\"traffic\" class=\""+col+"\"><font class=\"traffichead\">"+title+"</font><br />"+text+"</div>"
        return htm
         
    def successbox(self, text,start="<br />",end=""):
        return "%s<div class=\"green\">%s</div>%s" % (start,text,end)
        
    def errorbox(self, text,start="<br />",end=""):
        return "%s<div class=\"red\">%s</div>%s" % (start,text,end)

    def notifybox(self, text,start="<br />",end=""):
        return "%s<div class=\"amber\">%s</div>%s" % (start,text,end)
