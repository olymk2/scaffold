from scaffold.core.widget import base_widget

class control(base_widget):

    def create(self, title):
        self.title = title

    def append(self, name, params, docs):
        self.content.append((name, params, docs))

    def render(self):
        htm = '<h2>%s</h2>' % self.title
        for name, params, docs in self.content:
            htm += '<h3>%s</h3>' % name
            htm += '<div>%s</div>' % name
            htm += '<div>%s</div>' % name
        return htm

