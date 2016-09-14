from ...core.widget import base_widget


class control(base_widget):  
    def __init__(self):
        self.data = []
        
    def create(self, htm):
        self.data = []
        self.data.append(htm)
        return self
    
    def append(self, htm):
        self.data.append(htm)
        return self

    def render(self):
        self.count += 1
        return "<pre>%s</pre>" % "\n".join(self.data)
