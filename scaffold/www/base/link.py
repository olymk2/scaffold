from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    content = []
    
    def start(self):
        self.content = []
        return self

    def reset(self):
        self.reset_attributes()
        self.content = []
        return self

    def create(self, title, content, link):
        self.reset()
        self.append(title, content, link)
        return self

    def append(self, title, content, link):
        self.content.append((title, content, link,))
        return self

    def render(self):
        htm = []
        for item in self.content:
            htm.append(u"""<a title="%s" href="%s" %s>%s</a>\n""" % (item[0], item[2], self.get_attributes(), item[1]))
        return self.seperator.join(htm)
