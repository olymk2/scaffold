from ...core.widget import base_widget


class control(base_widget):  
    list=[]
    count=0
    filename=''
    includes=[]
    includes.append('<script type="text/javascript" src="/themes/web/js/webgl/glMatrix-0.js"></script>')
    includes.append('<script type="text/javascript" src="/themes/web/js/webgl/webgl-utils.js"></script>')
    includes.append('<script type="text/javascript" src="/themes/web/js/webgl/openglShaders.js"></script>')
    includes.append('<script type="text/javascript" src="/themes/web/js/webgl/openglModelLoader.js"></script>')
    includes.append('<script type="text/javascript" src="/themes/web/js/webgl/openglScene.js"></script>')
    
    width=200
    height=200

    def javascript(self):
        js=("",)
        return "\n".join(js)
        
    def xhtmlbody(self,text,start="<br />",end=""):
        return ""
    
    def filepath(self,path):
        self.filename=path

    def render(self,id="webgl",htm=""):
        self.count+=1
        self.beenUsed=True
        return '''<div class="webgl" style="float:left;">%s<br />
            <a href="%s">
                <canvas id="webgl%d"  style="border: 2px solid #0000ff;" width="200" height="200"></canvas>
            </a>
        </div>''' % (self.filename,self.filename,self.count)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=()
        return "\n".join(htm)

    def html5head(self):
        return ""
