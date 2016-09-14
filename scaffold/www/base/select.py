import os
import sys
from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    rows = []
    label = ''

    def create(self, name, label='', node_id=None, node_class='menu'):
        self.rows = []
        self.label = label
        self.reset_attributes()
        self.node_attrs[0][1] = node_id
        self.node_attrs[1][1] = node_class
        self.node_attrs.append(['name', name])
        return self

    def append(self, value, text, selected=None):
        if selected is True or selected == value:
            self.rows.append('<option selected="selected" value="%s">%s</option>' % (value, text))
        else:
            self.rows.append('<option value="%s">%s</option>' % (value, text))
        return self

    def append_list(self, values):
        for value, text, selected in values:
            self.append(value, text, selected=None)
        return self

    def render(self):
        return '<label for="%s">%s</label><select %s>%s</select>' % (self.node_attrs[-1][1], self.label ,self.get_attributes(), "\n".join(self.rows))

