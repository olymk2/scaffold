from ...core.widget import base_widget


class control(base_widget):  
    boxes_per_row=3
    frame=''
    css_class="boxgrid"
    list=[]
    links=[]

    def javascript(self):
        js=("",)
        return "\n".join(js)

    def create(self, title, link, img, details=()):
        self.links.append((title, link, img, details))

    def append(self, title, link, img, details=()):
        self.links.append((title, link, img, details))
        
    def render(self,items=(),cols=2):
        count=0
        tc=0
        columns=[]
        htm="<div class=\"list\">"
        width=str(90/(cols+1))
        
        count=0

        for title,link,img,details in self.links:
            htm+="<div class=\"box\">"
            htm+="<a title=\""+title+"\" href=\""+link+"\">"            
            htm+="<span class=\"thumb\">"

            htm+="<span class=\"frame\"><img alt=\"\" src=\""+self.frame+"\" /></span>"
            htm+="<img alt=\""+title+"\" src=\""+img+"\" />"
            htm+="</span>"
            htm+="<span class=\"title\">"
            htm+="<span>Suzuki Alto</span>"
            htm+="</span>"
            htm+="</a>"
            htm+="</div>"
        htm+="</div>"
        self.links=[]
        self.list=[]
        return htm 

