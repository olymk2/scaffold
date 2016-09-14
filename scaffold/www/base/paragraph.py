from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    data = []

    def create(self, htm):
        self.data = [[]]
        self.append(htm)
        return self

    def append(self, htm):
        self.data[-1].append(htm)
        return self
    
    def add(self, htm):
        self.data.append([])
        self.append(htm)
        return self

    def render(self):
        self.count += 1
        return ''.join(['<p>' + ''.join(p) + '</p>' for p in self.data])
