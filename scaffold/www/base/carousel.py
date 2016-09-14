from ...core.widget import base_widget


class control(base_widget):  
    view=[]
    buttons=[]
    count=0
    offset=60
    height=300
    width=800
    includes=[]
    includes.append('<script type="text/javascript" src="/themes/web/js/jquery/jquery.banners.js"></script>');
    path=''
    small=[]
    medium=[]
    folders=('thumbs','medium','large')
    
    def javascript(self):
        js=("$(document).ready(function(){",
            "\t$('.bannerFlip').bannerflip();",
            "});")
        return "\n".join(js)+"\n"
    
    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]
        self.medium=[]

    def set_folders(self,folders=('thumbs','medium','large')):
        self.folders=folders

    def append(self,image,path):
        self.small.append('<a href="%s" ><img src="%s" /></a>'%(self.path+self.folders[2]+image,self.path+self.folders[0]+image))
        self.medium.append('<a href="%s" ><img src="%s" /></a>'%(self.path+self.folders[2]+image,self.path+self.folders[0]+image))

    def render(self):   
        self.count+=1
        htm='<div class="carousel">'
        htm+='<div class="medium">'+''.join(self.medium)+'</div>'
        
        htm+='<ul style="height:%dpx;width:%dpx">' % (self.height,self.width)
        count=0
        for item in self.content:
            htm+='<li style="left:%dpx;">%s</li>' % (self.offset*count,item)
            count+=1
        htm+='<li style="clear:both;"></li>'
        htm+='</ul></div><div class="clear"></div>'
        return htm
