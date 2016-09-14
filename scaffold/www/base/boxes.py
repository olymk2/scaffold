
from ...core.widget import base_widget


class control(base_widget):  
    buttonlist=[]
    node_class='box'
    node_class_list=['boxlist']
    count=0
    size=3
    
    
    def javascript(self):
        js=("",)
        return "\n".join(js)
    
    def create(self,id=None,width=None,height=None):
        self.html=[]
    
    def append(self,text,id="",title=""):
        self.buttonlist.append((text,id,title))
        
    def render(self):
        htm='<div class="%s">' % self.node_class_list
        item=0
        
        for text in self.html:
            if item%self.size==0:
                htm+='<div class="end %s ">%s</div>' %(self.get_class(),text)
            else:
                htm+='<div class="%s ">%s</div>' %(self.get_class,text)
            item+=1
            self.count+=1
        htm+='<div class="clear"></div></div>'
        self.buttonlist=[]
        self.html=[]
        return htm
