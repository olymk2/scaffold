from ...core.widget import base_widget_extended


class control(base_widget_extended):
    title = ''
    sections = []
    foot = ''
    id = ''

    def create(self, title, node_id=None, node_class='page'):
        self.reset_attributes()
        self.node_attrs[0][1] = node_id
        self.node_attrs[1][1] = node_class
        self.sections = []
        self.title = title
        self.foot = ''
        return self

    def header(self, head):
        self.title = head
        return self

    def add(self, content, id=None):
        self.sections.append((id, []))
        self.sections[-1][1].append(content)
        return self

    def section(self, content, id=None):
        self.sections.append((id, []))
        self.sections[-1][1].append(content)
        return self

    def append(self, content):
        self.sections[-1][1].append((content))
        return self

    def render(self):
        self.count += 1
        htm=u"""<div%s>\n""" % self.get_attributes()
        htm+=u"""<header class="pageHeader">\n\t%s</header>\n""" % self.title
        for s in self.sections:
            if s[0]:
                htm+=u"""<section id=\"%s\" class="pageSection">\n\t%s</section>\n""" %(s[0],''.join(s[1]))
            else:
                htm+=u"""<section class="pageSection">\n\t%s</section>\n""" % ''.join(s[1])

        htm+=u"""<footer class="pageFooter">\n\t%s</footer>\n""" % self.foot
        htm+=u"""</div>\n"""
        return htm
