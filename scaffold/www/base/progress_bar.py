from ...core.widget import base_widget


class control(base_widget):  
    bars=[]
    count=0
  
    def javascript(self):
        js=("",)
        return "\n".join(js)
    
    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]
     

    #not implemented yet but could pass two values and work out percentage from there
    def append_value(self,link,image,text,msgbox=None):
        pass

    #pass in title and percentage 
    def append(self,title,percent):     
        htm ='<div>'
        htm+='<div class=\'pbouter\'>'
        htm+='<div class=\'pbinner\' style=\'width:'+percentage+'%\'>'+title+' Using '+percentage+'</div>'
        htm+='</div>'
        htm+='</div>'
        self.bars.append(htm)


    def render(self):   
        return ''.join(self.bars)


