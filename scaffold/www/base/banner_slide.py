from ...core.widget import base_widget


class control(base_widget):  
    view=[]
    buttons=[]
    content=[]
    count=0
    offset=60
    height=300
    width=400
    
    def javascript(self):
        js=("",)
        return "\n".join(js)
    
    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]

    def append(self,image,link,title,intro=''):
        htm='<a href="%s" ><img src="%s" /><div class="content">%s<br />%s</div></a>'%(link,image,title,intro)
        self.content.append(htm)

    def render(self):   
        self.count+=1
        htm='<div class="banner-slide">'
        htm+='<ul style="%s">' % self.height
        count=0
        for item in self.content:
            htm+='<li style="left:%dpx;">%s</li>' % (self.width*count,item)
            count+=1
        htm+='<li style="clear:both;"></li></ul>'
        htm+='<div title="Previous" class="left"></div><div title="Next" class="right"></div>'
        htm+='</div><div class="clear"></div>'
        return htm
