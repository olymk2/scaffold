from ...core.widget import base_widget


class control(base_widget):  
    id='notify'
    notify_count=0
    notifylist=[]
    def javascript(self,id=None):
        js=("",)
        return "\n".join(js)
        
    def append(self,htm):
        self.notifylist.append(htm)

    def render(self):
        self.notify_count+=1
        return "<div id=\"%s%d\" class=\"%s\">%s</div>" %(self.id,self.notify_count,self.id,"".join(self.notifylist))
