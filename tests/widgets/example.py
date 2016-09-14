from scaffold.core.widget import base_widget

class control(base_widget):
    script = ['var test="hello world";']

    def test_uri_access(self):
        return self.uri

    def render(self):
        htm = '<div id="example"></div>'
        return htm
