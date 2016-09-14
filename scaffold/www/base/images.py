from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    images = []
            
    def create(self, image, title=''):
        self.images = []
        self.html = []
        self.reset_attributes()
        self.append(image, title)
        return self
        
    def append(self, image, title=''):
        self.images.append((image, title))
        return self

    def render(self):
        self.html = []
        for img in self.images:
            self.html.append("""<img src="%s" alt="%s" %s/>\n""" % (img[0],img[1],self.get_attributes()))
        return "\n".join(self.html)
