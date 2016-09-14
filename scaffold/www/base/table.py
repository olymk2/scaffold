from ...core.widget import base_widget_extended


class control(base_widget_extended):  
    tableid = ''
    title = ''
    rowlist = []

    classcurrent = 0
    classcount = 2
    classlist = 'tabrow1', 'tabrow2'
    column_class_list = []
    header_classlist = None

    class_id = 'class="tab"'
    def javascript(self):
        js = ("", )
        return "\n".join(js)

    def reset(self):
        self.column_class_list=[]
        self.rowlist=[]

    def create(self, title="", header=(), footer=(), id="table"):
        """Create a new table / reset table.

        Args:
            table title,headers as a list or tuple,footer as a list or tuple,unique id of the table.
        Returns:
            Nothing
        """

        self.reset()
        self.set_id('%s%d' % (id, self.count))

        self.title = title
        self.table_header = header
        self.table_footer = footer
        return self

    def append(self, columns, header=None):
        """Append Row to the table.

        Args:
            tuple / list of row cells,optional header.
        Returns:
            Nothing
        """
        self.rowlist.append([header] + list(columns))
        return self

    def __iter__(self):
        for row in self.rowlist:
            yield row

    def render(self):
        """Generates tables html
        Args:
            None
        Returns:
            string
        """
        self.count += 1
        #tableid="%s%d" % (id,self.table_count)

        lh = len(self.table_header)
        lf = len(self.table_footer)
        lt = 0

        htm = u"<table %s>\n" % self.get_attributes()
        htm += u"<caption class=\"tabtitle\">%s</caption>\n" % self.title
        if lh != 0:
            htm += u"<thead><tr class=\"tabhead\"><th>%s</th></tr></thead>" % u"</th><th>".join(self.table_header)
        if lf != 0:
            htm += u"<tfoot><tr><td>%s</td></tr></tfoot>" % u"</td><td>".join(self.table_footer)
        htm += u"<tbody>\n"

        for row in self.rowlist:
            header=row[0]

            if header:
                htm+=u"<tr class=\"%s\"><td>" % (self.classlist[self.classcurrent]) + u"<th>%s</th>" % header
            else:
                values = u""
                for item in row[1:]:
                    values += u"<td>" + item + u"</td>" 
                htm+=u"<tr class=\"%s\">" % (self.classlist[self.classcurrent]) + values + u"</tr>"

            self.classcurrent+=1
            if self.classcurrent==self.classcount:
                self.classcurrent=0
        htm+=u"\n</tbody></table><br />\n"
        return htm


    def xhtmlhead(self):
        return ""


    def html5head(self):
        return ""

    def __unit_tests(self):
        #example of creating a table
        print("First Table Test")
        self.create('My Table Title',('Column 1','Column 2','Column 3','Column 4','Column 5'))
        for row in range(0,6):
            self.append([row,'a','b','c','d'])
        return self.render()


