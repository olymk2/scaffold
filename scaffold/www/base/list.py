from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    frame = ''
    css_class = "list"
    content = []

    node_start = '<ol>'
    node_end = '</ol>'

    def create(self, text=None, ordered=True):
        self.count += 1
        self.content = []
        if text:
            self.append(text)
        if ordered is True:
            self.node_start = '<ol%s>' % self.get_attributes()
            self.node_end = '</ol>'
        else:
            self.node_start = '<ul%s>' % self.get_attributes()
            self.node_end = '</ul>'
        return self

    def append(self, text):
        self.content.append(text)
        return self

    def render(self):
        htm = []
        htm.append(self.node_start)
        for item in self.content:
            htm.append('<li>' + item + '</li>')
            
        htm.append(self.node_end)
        self.content = []
        return "\n".join(htm)
