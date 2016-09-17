from ...core.widget import base_widget


class control(base_widget):  
    link = 'myurlhere'
    analytics_code = 'UA-XXXXXXXX-X'
    script = []

    def create(self, url, code):
        self.script = []
        self.link = url
        self.analytics_code = code

    def render(self):
        self.count += 1
        self.script.append("""\n(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                \n(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                \nm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                \n})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
                \n\nga('create', '%s', '%s');
                \nga('send', 'pageview');""" % (self.analytics_code, self.link))
        return '<!--google analytics-->'
