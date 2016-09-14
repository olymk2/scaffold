from ...core.widget import base_widget


class control(base_widget):  
    buttonlist=[]
    node_class='class="buttons"'
    
    
    def javascript(self):
        js=("",)
        return "\n".join(js)
        
    def xhtmlbody(self,text,start="<br />",end=""):
        return ""

    def append(self,link,img,text,id=''):
        if id:
            id='id="'+id+'"'
        self.buttonlist.append((link,img,text,id))

    def render(self):
        htm='<div %s>' % self.node_class

        for b in self.buttonlist:
            htm+="<a href=\""+b[0]+"\" "+b[3]+">"
            htm+="<img src=\""+b[1]+"\" alt=\""+b[2]+"\"/>"
            htm+="</a>"
        htm+='</div>'
        self.buttonlist=[]
        return htm
