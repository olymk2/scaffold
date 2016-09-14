from ...core.widget import base_widget


class control(base_widget):  
    featureCount=0        
    def javascript(self):
        js=(    "var map, locations, controls, select;",
                "var extent = new OpenLayers.Bounds(-180, -90, 180, 90);",

            "addLoadEvent(init_map);",)
        self.jscript=True
        return "\n".join(js)
    
    def create(self, name):
        self.name = name

    def render(self):
        width=600
        height=300
        self.name='map'
        #if('width' in dict):
        #    width=dict['width']

        #if('height' in dict):
        #    height=dict['height']
        
        htm=(   "<label for=\""+self.name+"\"></label><div id=\""+self.name+"\" style=\"height:%spx; width:%spx;\"></div>" %(height,width),
                "<input type=\"hidden\" usm:valformat=\"n*\" id=\""+self.name+"_long\" self.name=\""+self.name+"_long\" />",
                "<input type=\"hidden\" usm:valformat=\"n*\" id=\""+self.name+"_lat\" self.name=\""+self.name+"_lat\" />")
        
        return "\n".join(htm)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
