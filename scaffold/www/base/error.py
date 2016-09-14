from ...core.widget import base_widget


class control(base_widget):  
    errorlist=[]
    def javascript(self):
        js=("",)
        return "\n".join(js)
            
    def append(self,htm):
        self.errorlist.append(htm)

    def render(self):
        self.count+=1
        return "<pre>%s</pre>" %("\n".join(self.errorlist))

