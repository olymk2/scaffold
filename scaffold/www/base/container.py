from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    count = 0

    def create(self, content='', node_id=None, node_class=None):
        self.content = []
        self.reset_attributes()
        self.node_attrs[0][1] = node_id
        self.node_attrs[1][1] = node_class
        self.content.append(content)
        return self

    def append(self, htm):
        if self.content:
            self.content[-1] += htm
        return self

    def add(self, content=''):
        self.content.append(content)
        return self

    def render(self):
        return '<div%s>%s</div>' % (self.get_attributes(), "".join(self.content))
