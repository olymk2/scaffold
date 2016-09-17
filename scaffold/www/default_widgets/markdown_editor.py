from scaffold.core.widget import base_widget


class control(base_widget):
    includes = []
    script = []
    css = base_widget.uri.ful + '../scaffold/www/default_widgets/css/simplemde.css'
    
    def __init__(self):
        self.includes = [
            """<script type="text/javascript" src="file:%sjs/simplemde.min.js"></script>""" % base_widget.uri.med,
            """<link rel="stylesheet" href="file:%scss/simplemde.min.css">""" % base_widget.uri.med]
        self.script = ['$(document).ready(function(){var simplemde = new SimpleMDE({ element: $("#simplemde")[0]});});',]
    
    def create(self):
        return self

    def render(self):
        super(control, self).render()
        return """<textarea id="simplemde" class="simplemde"></textarea>"""
