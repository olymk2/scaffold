from ...core.widget import base_widget

import gettext
gettext.bindtextdomain('usm', './lang/')
gettext.textdomain('usm')
_ = gettext.gettext

class control(base_widget):  
    title=_('Please login to access this content')
    description=_('')
    msg=_('Please enter your username and password to continue')
    page=''
    subpage=''
    db=''
    
    data_total = 0.0
    data_max = 0
    data_min = 0
    data = []

    show_open_id = False
    def create(self, text=None, data_max=100):
        if text:
            self.title = _(text)

    def append(self, start, end, title=''):
        self.data_total = float(max(end,self.data_total))
        self.data.append((start, end, title))
        
    def render(self, html=""):
        htmout='<div style="background-color:#fff;width:100%;height:200px;position:relative;">'
        count = 0
        for start, end, title in self.data:
            left = (start / self.data_total) * 100.0
            end = ((end / self.data_total) * 100.0) - left
            htmout+='<div style="background-color:#000;position:absolute;top:%spx;left:%s%%;height:20px;width:%s%%;" title="%s"></div>' % (count,left,end, title)
            count += 25
        
        htmout+='</div>'    
        return htmout
     

