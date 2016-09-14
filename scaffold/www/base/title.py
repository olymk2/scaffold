from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    level = '1'
    tag_start = '<h1>'
    tag_end = '</h1>'
    tag_split = '<h1></h1>'
    
    def create(self, htm, level='2'):
        self.data = []
        self.level = level
        self.data.append(htm)
        self.tag_start = '<h%s>' % level
        self.tag_end = '</h%s>' % level
        self.tag_split = self.tag_start+self.tag_end
        return self

    def append(self, htm):
        self.data.append(htm)
        return self

    def render(self):
        self.count += 1
        return '<h%s>%s</h%s>' % (self.level, self.tag_split.join(self.data), self.level) 
        #~ return '<h%s>%s</h%s>'(self.tag_start + "%s" + self.tag_end) % self.tag_split.join(self.data)
