from ...core.widget import base_widget


class control(base_widget):  
    view=[]
    buttons=[]
    content=[]
    count=0
    offset=60
    height=300
    menu=[]
    submenu=[]
        
    def javascript(self):
        js=("",)
        return "\n".join(js)
    
    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]

    def append(self,link,title,image,intro=''):
        
        
        menu="<div class=\"mi\">"
        menu+="<img alt=\"mi\" src=\""+icon+"\" />"
        if link[0:4]=="http":
            menu+="<a href=\""+str(link)+"\" >"+str(friendly)+"</a><br />"
        elif link[0:8]=="index.py":
            menu+="<a href=\""+str(link)+"\" >"+str(friendly)+"</a><br />"
        else:
            menu+="<a href=\""+str(link)+"\" >"+str(friendly)+"</a><br />"
        menu+="</div>\n"
        submenu.append(menu)

    def append_submenu(self):
        menu="".join(self.submenu)

    def render(self):   
        self.count+=1
        htm='<div class="bannerFlip"><ul style="%s">' % self.height
        count=0
        for item in self.content:
            htm+='<li style="left:%dpx;">%s</li>' % (self.offset*count,item)
            count+=1
        htm+='<li style="clear:both;"></li>'
        htm+='</ul></div><div style="clear:both;"></div>'
        return htm
