from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    content = []

    def create(self, htm, node_id=None, node_class=None):
        self.content = []
        self.reset_attributes()
        self.node_attrs[0][1] = node_id
        if node_class:
            self.node_attrs[1][1] = node_class
        self.content.append(htm)
        return self

    def append(self, htm):
        self.content.append(htm)
        return self

    def render(self):
        self.count += 1
        return "<div%s>%s</div>" % (self.get_attributes(), ''.join(self.content))
