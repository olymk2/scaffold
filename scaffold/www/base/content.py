from ...core.widget import base_widget


class control(base_widget):  
    code=[]
    paragraphs=[]
    
    def javascript(self):
        js=("",)
        return "\n".join(js)
    
    #legacy
    def table_start(self,title="",header=(),footer=(),id="table"):
        self.start(title,header,footer,id)
    
    def create(self,title="",header=(),footer=(),id="table"):
        """Create a new table / reset table.

        Args:
            table title,headers as a list or tuple,footer as a list or tuple,unique id of the table.
        Returns:
            Nothing
        """
        self.rowlist=[]
        self.tableid="%s%d" % (id,self.count)
        
        self.title=title
        self.header=header
        self.footer=footer

    def append(self,columns,header=None):
        """Append Paragraph.

        Args:
            tuple / list of row cells,optional header.
        Returns:
            Nothing
        """
        self.rowlist.append([header]+columns)

    def __iter__(self):
        for row in self.rowlist:
            yield row

    def clear(self):
        self.rowlist=[]

    def render(self):
        """Generates tables html
        Args:
            None
        Returns:
            string
        """
        self.count+=1
        #tableid="%s%d" % (id,self.table_count)
        
        lh=len(self.header)
        lf=len(self.footer)
        lt=0
        
        htm="<table id=\"%s\" class=\"tab\">\n"%self.tableid
        htm+="<caption class=\"tabtitle\">%s</caption>\n"% self.title
        if lh!=0:
            htm+="<thead><tr class=\"tabhead\"><th>%s</th></tr></thead>" %"</th><th>".join(self.header)
        if lf!=0:
            htm+="<tfoot><tr><td>%s</td></tr></tfoot>"%"</td><td>".join(self.footer)
        htm+="<tbody>"
    
        for row in self.rowlist:
            header=row[0]
            
            htm+="<tr class=\"%s\">" % self.classlist[self.classcurrent]
            if header:
                htm+="<th>%s</th>" % header
            for c in row[1:]:
                htm+="<td>%s</td>" % c
            self.classcurrent+=1
            if self.classcurrent==self.classcount:
                self.classcurrent=0
            #self.style=self.switch_style(self.style,"tabrow1","tabrow2")
            #self.list.append("<tr><td>%s</td></tr>"%htmout)
            htm+="</tr>"

            #return htmout+"</tr>\n"
        
        htm+="\n</tbody></table><br />\n"
        self.rowlist=[]
        return htm


    def xhtmlhead(self):
        return ""


    def html5head(self):
        return ""


