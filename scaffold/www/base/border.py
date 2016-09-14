
from ...core.widget import base_widget


class control(base_widget):  
    slideable=True
    hidden=True
    list=[]
    htmtitle=''
    htmbody=''
    htmfooter=[]
    js={}
    
    def javascript(self):
        return ""
    
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

    def corners(self,html):
        htm=(   "<div class=\"border\">",
                "<div class=\"content\">%s</div>"% html,
                "<div class=\"tl\"></div>",
                "<div class=\"tr\"></div>",
                "<div class=\"bl\"></div>",
                "<div class=\"br\"></div>",
                "</div>")
        return "\n".join(htm)

    def render(self,html=""):
        htm=(   "<div class=\"border\">",
                "<div class=\"content\">%s</div>"% html,
                "<div class=\"tl\"></div>",
                "<div class=\"tr\"></div>",
                "<div class=\"bl\"></div>",
                "<div class=\"br\"></div>",
                "<div class=\"te\"></div>",
                "<div class=\"be\"></div>",
                "<div class=\"le\"></div>",
                "<div class=\"re\"></div>",
                "</div>")
        return "\n".join(htm)

    def xhtmlhead(self):
        return ""        

