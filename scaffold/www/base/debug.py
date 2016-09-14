import pprint
from ...core.widget import base_widget


class control(base_widget):  
    list=[]
    def javascript(self):
        js=("",)
        return "\n".join(js)
            
    def append(self,htmlist):
        for item in htmlist:
            self.list.append(item)
            
            if item == 'subform':
                for item2 in htmlist[item]:
                    self.list.append("\t"+str(item2)+"\n\t\t\t"+str(item2))
                    if item2=='subformlist':
                        for formnodes in htmlist[item][item2]:
                            self.list.append("\t"+str(formnodes)+"\n\t\t\t")
            else:
                self.list.append(item+"\n\t"+str(htmlist[item]))

    def linebreak(self,list):
        for item in self.list:
            if item =={}:
                pass

    def render(self,id="notify",htm=""):
        self.count+=1
        return "Debug Result<br /><pre>%s</pre>" %("\n".join(self.list))

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)
