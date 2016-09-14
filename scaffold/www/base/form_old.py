import os
import sys
from .. import forms
from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    html_start = ''
    html_end = ''
    html_row_start = '<p>'
    html_row_end = '</p>'

    rows = []

    def create(self, action, method='post', enctype='multipart/form-data', node_id=None, node_class='menu'):
        self.rows = []
        self.reset_attributes()
        self.node_attrs[0][1] = node_id
        self.node_attrs[1][1] = node_class
        self.node_attrs.append(['action', action])
        self.node_attrs.append(['enctype', enctype])
        self.node_attrs.append(['method', method])

    def append(self, item):
        self.rows.append(item)

    def spacer(self, name):
        self.rows.append("</fieldset><fieldset id=\"%s\">\n" % (name))

    def render(self):
        self.html = []
        self.html.append('<form %s><fieldset>' % self.get_attributes() + self.html_start)
        for row in self.rows:
            self.html.append(self.html_row_start + row + self.html_row_end)
        self.html.append(self.html_end + '</fieldset></form>')
        return "\n".join(self.html)

