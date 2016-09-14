from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    titles = []
    content = []
    tab_count = 1
    tab_id = '#tabs-'


    def create(self, title=None, content=None, link=None, node_id=None, node_class=None):
        self.titles = []
        self.content = []

        self.reset_attributes()
        self.node_attrs[0][1] = node_id
        self.node_attrs[1][1] = node_class
        if title:
            self.append(title=title, content=content)
        return self

    def set_tab_id(self, name):
        self.tab_id = name
        return self

    def append(self, title, content, link=None):
        self.titles.append('<li><a href="%s">%s</a></li>' % (self.tab_id + str(self.tab_count), title))
        self.content.append('<div id="%s">%s</div>' % (self.tab_id.strip('#') + str(self.tab_count), content))
        self.tab_count += 1
        return self

    def render(self):
        self.count += 1
        return '<div%s><ul>%s</ul>%s</div>' % (self.get_attributes(), ''.join(self.titles), ''.join(self.content))
