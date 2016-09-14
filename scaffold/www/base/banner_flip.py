from ...core.widget import base_widget


class control(base_widget):  
    view=[]
    buttons=[]
    content=[]
    count=0
    offset=60
    height=300
    width=800
    includes=[]
    includes.append('<script type="text/javascript" src="/themes/web/js/jquery/jquery.banners.js"></script>');
    
    def javascript(self):
        js=("$(document).ready(function(){",
            "\t$('.bannerFlip').bannerflip();",
            "});")
        return "\n".join(js)+"\n"
    
    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]

    def append(self,image,link,title,intro=''):
        htm='<a href="%s" ><img src="%s" /><div class="content">%s<br />%s</div></a>'%(link,image,title,intro)
        self.content.append(htm)

    def render(self):   
        self.count+=1
        htm='<div class="bannerFlip"><ul style="height:%dpx;width:%dpx">' % (self.height,self.width)
        count=0
        for item in self.content:
            htm+='<li style="left:%dpx;">%s</li>' % (self.offset*count,item)
            count+=1
        htm+='<li style="clear:both;"></li>'
        htm+='</ul></div><div class="clear"></div>'
        return htm
