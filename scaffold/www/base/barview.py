from ...core.widget import base_widget


class control(base_widget):  
    view=[]
    buttons=[]
    content=[]
    count=0
  
    def javascript(self):
        js=("",)
        return "\n".join(js)
    
    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]

    def create(self, left, centre=None, right=None):
        self.content = []
        self.content.append((left, centre, right,))

    def append(self, left, centre=None, right=None):
        #self.content.append( "<div>%s</div>" %(text))
        self.content.append((left, centre, right,))

    def append_view(self,link,image,text,msgbox=None):
        if msgbox is not None:
            self.view.append( "<div class=\"button\"><a class=\"buttonlink\" href=\"%s\" onclick=\"confirm('%s')\"><img src=\"%s\" alt=\"%s\" />%s</a></div>" %(link,msgbox,image,text,text))
        else:
            self.view.append("<div class=\"button\"><a class=\"buttonlink\" href=\"%s\"><img src=\"%s\" alt=\"%s\" />%s</a></div>" %(link,image,text,text))


    def append_button(self,link,image,text,msgbox=None):
        
        if msgbox is not None:
            self.buttons.append( "<div class=\"button\"><a class=\"buttonlink\" href=\"%s\" onclick=\"confirm('%s')\"><img src=\"%s\" alt=\"%s\" />%s</a></div>" %(link,msgbox,image,text,text))
        else:
            self.buttons.append("<div class=\"button\"><a class=\"buttonlink\" href=\"%s\"><img src=\"%s\" alt=\"%s\" />%s</a></div>" %(link,image,text,text))




    def render(self):   
        self.count+=1
        htm=''
        for row in self.content:
            htm+="\n<div id=\"boxrow%d\" class=\"boxrow\" >" % self.count
        
            htm+="<div id=\"brl%d\" class=\"left\" >%s</div>" % (self.count,row[0])
            if row[1] is not None:
                htm+="<div id=\"brm%d\" class=\"middle\" >%s</div>" % (self.count,row[1])
            if row[2] is not None:
                htm+="<div id=\"brr%d\" class=\"right\" >%s</div>" % (self.count,row[2])
            htm+="</div>\n" 
        self.reset()         
        return "<div class=\"container\">%s</div>\n" % "".join(htm)


