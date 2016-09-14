from scaffold.core.widget import base_widget

class control(base_widget):
    root = '/'

    def create(self, root='/'):
        self.content = []
        self.root = root
        return self

    def __mul__(self, items):
        for row in items:
            self.append(row)

    def render(self):
        htm = '<ul>'
        if len(self.content) < 1:
            htm += '<li><a href="/">Home</a></li>'
        path = ''
        for crumb in self.content[0:-1]:
            path += crumb + '/'
            htm += '<li><a href="%s%s">%s</a></li>' % (self.root, path, crumb.title())
        htm += '</ul>'
        return htm

