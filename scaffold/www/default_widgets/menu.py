from ...core.widget import base_widget_extended
from ...loaders import load_resource

class control(base_widget_extended):  
    css = '../scaffold/www/default_widgets/css/menu.css'
    js = 'menu.js'
    menu = []
    selected = None
    
    def create(self, select=None):
        self.menu = []
        #~ self.reset_attributes()
        #~ self.node_attrs[0][1] = node_id
        self.node_attrs[1][1] = 'menu'
        self.selected = select
        return self

    def append(self, title, link, submenu=None):
        """Append item to menu.

        Args:
            link title, link url
        Returns:
            Nothing
        """
        self.menu.append((title, link))

    def render(self):
        htm = '<nav%s>\n\t<ul>\n' % self.get_attributes()
        menu_count = 0
        for title, link in self.menu:
            if link == self.selected:
                htm += '\t\t<li class="active mi%d"><a href="%s" >%s</a></li>\n' % (menu_count, link, title)
            else:
                htm += '\t\t<li class="mi%d"><a href="%s" >%s</a></li>\n' % (menu_count, link, title)
            menu_count += 1
        htm += '\t</ul>\n<div style="clear:both;"></div>\n</nav>'
        return htm
