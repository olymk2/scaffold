from ...core.widget import base_widget


class control(base_widget):  
    boxes_per_row=3
    css_class="boxgrid"
    list=[]
    links=[]

    def javascript(self):
        js=("",)
        return "\n".join(js)
        
    #multiple plain text or numerical data form input
    def xhtmlbody(self,text,start="<br />",end=""):
    #def notifybox(self, text,start="<br />",end=""):
        return "%s<div class=\"amber\">%s</div>%s" % (start,text,end)
    
    def append_link(self,title,link):
        self.links.append((title,link))
        
    def append_box(self,title,img,link):
        self.list.append((title,img,link,self.links))
        self.links=[]
        #items=("/images/icons/tango/32x32/devices/input-gaming.png","My Server Info",self.links),
        #items+=("/images/icons/tango/32x32/categories/applications-system.png","Server settings","Change Themes Profiles / Manage access rights","index.py?Page=home&amp;subpage=server"),
        #items+=("/images/icons/tango/32x32/categories/applications-system.png","Sharing Services","Sharing of Folders Media and Devices like printers","index.py?Page=home&amp;subpage=shares"),
        

    def render(self,items=(),cols=2):
        count=0
        tc=0
        columns=[]
        htm=""
        width=str(90/(cols+1))
        
        count=0
        htm+="<div class=\"boxgridmain\"><div><div class=\"boxgridcontainer\" >"
        for title,img,mainlink,items in self.list:
            #htm=""
            htm+="\n<div id=\"boxgrid"+str(count)+"\" class=\"boxgrid\" style=\"float:left;\" onclick=\"document.location='"+mainlink+"';\">"
            #htm+="<a  href=\""+mainlink+"\">"
            htm+="<div style=\"background-image:url('"+img+"');\" class=\"boxselicon\">&#160;"
            htm+="<span class=\"boxseltitle\">"+title+"<br /></span><span class=\"boxseltext\"></span>"
            for text,link in items:
                htm+='<a href="'+link+'" >'+text+'</a><br />'
            htm+="</div>"



            htm+="</div>\n"
            #columns.append(htm)
        htm+="<div style=\"clear:both;\"></div>"
        htm+="</div></div><div style=\"clear:both;\"></div></div>"  
        self.links=[]
        self.list=[]
        return htm 

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""

    def boxrows(self,items=(),cols=2):
        htm="<div style=\"margin:auto;\">"
        for icon,title,msg,link in items:
            htm+="\n<div id=\"boxgrid"+str(count)+"\" class=\"boxgrid\" style=\"width:100%;\">"
            htm+="<div style=\"background-image:url('"+icon+"');\" class=\"boxselicon\">&#160;</div>"
            htm+="<div style=\"border:1px solid #0;\"> <span class=\"boxseltitle\">"+title+"<br /></span><span class=\"boxseltext\">"+msg+"</span></div>"
            htm+="<div style=\"background-image:url('"+icon+"');\" class=\"boxselbuttons\">&#160;</div>"
            htm+="</div>\n"
        htm="<div style=\"margin:auto;\">"
        htm+="</div>"
        return htm
