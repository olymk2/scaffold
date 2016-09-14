from ...core.widget import base_widget


class control(base_widget):  
    list = []

    def create(self, htm):
        self.list = []
        self.list.append(htm)
        return self

    def append(self, htm):
        self.list.append(htm)
        return self

    def render(self):
        self.count += 1
        return "<span>%s</span>" % "</span><span>".join(self.list)
