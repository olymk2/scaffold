from math import ceil
import sys
from ...core.widget import base_widget


class control(base_widget):   
    steps = True
    htmtitle = ''
    htmbody = ''
    htmfooter = []
    js = {}

    limit = 0
    total = 0
    page = 0
    current = 0

    first = '&laquo;'
    last = '&raquo;'
    previous = '&lt;'
    next = '&gt;'

    url_before = '/'
    url_after = '/'

    def javascript(self):
        return ""

    def reset(self):
        self.limit = 0
        self.total = 0
        self.page = 0
        self.current = 0

    def url(self,before,after):
        self.url_before = before
        self.url_after = after

    def create(self, perpage, total, page=1):
        """Create a new table / reset table.

        Args:
            items per page, total items, current page
        Returns:
            Nothing
        """
        if total > perpage:
            self.total = int(ceil(total / float(perpage)) + 1)
            self.limit = perpage
            self.current = page
        return self

    def render(self):
        """Generates html
        Args:
            None
        Returns:
            string
        """
        htm = '<div class = \"pagination\" >'
        if self.total>0:
            htm += "<ul>"
            if self.current != 1:
                htm += '<li><a title = "Previous Page" href = "'+self.url_before+'1/'+self.url_after+'">'+self.previous+'</a></li>'
            count = 1
            for p in range(1,self.total):
                if p == self.current:
                    htm += '<li><a title = "Page '+str(p)+str(self.current)+'" href = "'+self.url_before+str(p)+self.url_after+'" class = "active">'+str(count)+'</a></li>'
                else:
                    htm += '<li><a title = "Page '+str(p)+str(self.current)+'" href = "'+self.url_before+str(p)+self.url_after+'">'+str(count)+'</a></li>'
                count += 1
            if self.current != self.total:
                htm += '<li><a title = "Next Page" href = "'+self.url_before+str(self.current+1)+self.url_after+'">'+self.next+'</a></li>'
            
            htm += '</ul>'
            htm += '<div style = "clear:both;"></div>'
        htm += '</div>'
        self.reset()
        return htm
