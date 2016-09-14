#from libs.v4.www.forms.default import html_form_ui
from .default import html_form_ui
class control(html_form_ui):        
    def javascript(self,id=None):
        js=(    "var map, locations, controls, select;",
                #"var extent = new OpenLayers.Bounds(-180, -90, 180, 90);",
                "var startlong=0.33096;",
                "var startlat=51.50803;",
                "var startzoom=20;",
                "var features = new Array();",
                "function init(){",
                #"alert('map');",
                "var mapOptions = {",
                "   projection:'EPSG:4326', ",
                #map drag limits, stop dragging past div borders
                "   restrictedExtent: new OpenLayers.Bounds(-180, -90, 180, 90),",

                "   controls:[], units:'degrees', ",
                "   maxResolution: 0.703125, ",
                "   numZoomLevels:16 ",
                "};",
                "//create map base layer",
                "map = new OpenLayers.Map('map',mapOptions);",
                "var mapLayer = new OpenLayers.Layer.WMS( 'OpenLayers WMS', 'http://labs.metacarta.com/wms/vmap0?', {layers: 'basic', isBaseLayer:true});",
                "map.addLayer(mapLayer);",
                "//mapLayer = new OpenLayers.Layer.OSM.Osmarender('Osmarender');",
                "//map.addLayer(mapLayer);\n",
                
    
                "map.addControl(new OpenLayers.Control.PanZoomBar());",               
                "map.addControl(new OpenLayers.Control.LayerSwitcher());//switch maps layers",
                "map.addControl(new OpenLayers.Control.NavToolbar());",
                "map.addControl(new OpenLayers.Control.MousePosition());//show mouse longitude and laitude",
            
                "// set up the default styling for the vector layer",
                "var symbolizer = new OpenLayers.Style(",
                "   {   fillColor:'red', ",
                "       fillOpacity:'1',",
                "       pointRadius: '20',",
                "       graphicZIndex: '${zind}',",
                "       externalGraphic: 'https://127.0.0.1:1980/images/icons/tango/32x32/actions/go-down.png'",
                "   });",
                
                
                
                
                "// set up the select styling for the vector layer",
                "var selectStyle = new OpenLayers.Style({ fillColor: 'Green'});",
                #"var featureStyle = new OpenLayers.Style({ fillColor: 'Green'});",
                
                "// create the style map",
                "var styleMap = new OpenLayers.StyleMap({",
                "   'default':  symbolizer, ",
                "   'select':   selectStyle",
                "});",

                "// create map features", 
                "features[0] = new OpenLayers.Feature.Vector(new OpenLayers.Geometry.Point(0.33096,51.50803),{});",
                "features[0].attributes.description = 'Sydney';",
                
                

                
                "// Create a vector layer and give it your style map.",
                "var locations = new OpenLayers.Layer.Vector('Vector locations', {styleMap: styleMap, rendererOptions: {zIndexing: true} } );",
                "locations.addFeatures(features);       // loads the whole array of vector features",
                "map.addLayer(locations);",
                
                
                "var dragMarker = new OpenLayers.Control.DragFeature(locations,{'onComplete':onDragComplete});",
                "map.addControl(dragMarker);",
                "dragMarker.activate();",
                
                
                "// Create a select feature control and add it to the map.",
                "//var select = new OpenLayers.Control.SelectFeature(locations, {   hover: selectStyle,             // this will change the style on hover",
                "// onSelect: onFeatureSelect,      // this generates the popup on select (also on hover?)",
                "// onUnselect: onFeatureUnselect   // this removes the popup on exiting the feature",
                "//});",
                "//map.addControl(select);",
                "//select.activate();",
                
                "// build the drag feature code and add to map",
                "var controls = { drag: new OpenLayers.Control.DragFeature(locations)    };",
                "for(var key in controls) {",
                "    map.addControl(controls[key]);",
                "   var control=controls[key];",
                "   control.activate();",
                "}",
                

                "map.setCenter(new OpenLayers.LonLat(startlong, startlat), 3);",
            "}",

            "function onFeatureSelect(feature) {",
                 "// generate the framedCloud popup",
                 "selectedFeature = feature;",
                 "var popup = new OpenLayers.Popup.FramedCloud('feature',", 
                             "feature.geometry.getBounds().getCenterLonLat(),",
                             "null,",
                             "'<div style=\"font-size:9px;\"><br/>'+feature.attributes.description+",
                             "'<br/>Lat = '+feature.geometry.y+",
                             "'<br/>Long = '+feature.geometry.x+'<br/><br/></div>',",
                             "null,false,null);",
                 "feature.popup = popup;",
                 "map.addPopup(popup);",
            "}\n",
                    
            "function onFeatureUnselect(feature){",
                "\tmap.removePopup(feature.popup);",
                "\tfeature.popup.destroy();",
                "\tfeature.popup = null;",
            "}\n",
            
            "function onDragComplete(feature,pos){",
                "\tdocument.getElementById('map_long').value=feature.geometry.x;",
                "\tdocument.getElementById('map_lat').value=feature.geometry.y;",
            "};\n",)
            
            #"$(document).ready(function(){,
            #    "\t",
            #"})",)

        self.jscript=True
        return "\n".join(js)
    
    def get_value(self,name,value):
        return [value[name+'_long'],value[name+'_lat']]
    
    def render(self,name, dict, error=0):
        width=400
        height=300
        name='map'
        error_msg,style=self.form_error_notify(error)
        if('width' in dict):
            width=dict['width']

        if('height' in dict):
            height=dict['height']
        
        
        htm=("<div id=\""+name+"\" style=\"height:%spx; width:%spx;\"></div>" %(height,width),
            "<input type=\"hidden\" usm:valformat=\"n*\" id=\""+name+"_long\" name=\""+name+"_long\" />",
            "<input type=\"hidden\" usm:valformat=\"n*\" id=\""+name+"_lat\" name=\""+name+"_lat\" />",)
        
        form=self.form_node_wrap("\n".join(htm),name,'',null=False,msg=error_msg)
        return self.form_node_contain(name,form)

    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<label for=\""+id+"\"></label>",
                "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
