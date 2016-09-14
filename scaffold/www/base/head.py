from ...core.widget import base_widget


class control(base_widget):  
    title = ''
    list = []
    meta_list = {}
    script_list = []
    link_list  = []

    def create(self, title):
        self.list = []
        self.list.append(title)

    def meta(self, key, value):
        self.meta_list['key'] = value

    def links(self, key, value, title=None):
        if title:
            self.links_list.append('<link rel="%s" href="%s" title="%s"/>' % (key,value,title))
        else:
            self.links_list.append('<link rel="%s" href="%s" />' % (key,value))

    def script(self, href, scripttype='text/javascript'):
        self.links_list.append('<script type="%s" href="%s" title="%s"/>' % (scripttype,href))

    def append(self, htm):
        self.list.append(htm)

    def render(self):
        htm='<title>%s</title>\n' % self.title
        htm+='\n'.join(self.link_list)
        htm+='\n'.join(self.meta_list)
        return '<title>%s</title>\n' % "\n".join(self.list)
