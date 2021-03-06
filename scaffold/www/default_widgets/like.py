from scaffold.core.widget import base_widget

class control(base_widget):
    link = None
    action = ""
    includes = []
    script = []

    facebook = False
    twitter = False
    plus = False
    linkedin = False

    plus_script = False
    linkedin_script = False
    facebook_script = False
    twitter_script = False

    def create(self, url, plus=None, twitter=None, facebook=None, linkedin=None):
        self.url = url
        self.plus = plus
        self.twitter = twitter
        self.facebook = facebook
        self.linkedin = linkedin
        
        if plus is not None:
            if self.plus_script is False:
                self.plus_script = True
                if int(plus) > 0:
                    self.includes.append("""<script type="text/javascript" async="true" defer="defer" src="https://apis.google.com/js/platform.js?publisherid=%s"></script>""" % self.plus)
                else:
                    self.includes.append("""<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>""")
        if twitter is not None:
            if self.twitter_script is False:
                self.twitter_script = True
                self.footer.append("""
                    <script><!--//--><![CDATA[//><!--!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');\n//]]></script>""")

        if linkedin is not None:
            if self.linkedin_script is False:
                self.linkedin_script = True
                self.footer.append("""
                    <script src="//platform.linkedin.com/in.js" type="text/javascript"> lang: en_US</script>""") 

        if facebook is not None:
            if self.facebook_script is False:
                self.facebook_script = True
                self.footer.append("""
                    <div id="fb-root"></div><script><!--//--><![CDATA[//><!--(function(d, s, id) {var js, fjs = d.getElementsByTagName(s)[0];if (d.getElementById(id)) return;js = d.createElement(s); js.id = id;js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.3";fjs.parentNode.insertBefore(js, fjs);}(document, 'script', 'facebook-jssdk'));\n//]]></script>""") 
        return self

    def render(self):
        self.count += 1
        htm = '< !--like widgets-->'
        if self.twitter:
            htm += '<div class="socbut"><a href="https://twitter.com/share" class="twitter-share-button" data-via="%s">Tweet</a></div>' % self.twitter
        if self.facebook:
            htm += '<div class="socbut"><div class="fb-share-button" data-href="%s" data-layout="button_count" data-action="like" data-show-faces="true" data-share="true"></div></div>' % self.url
        if self.linkedin:
            htm += '<div class="socbut"><script type="IN/Share" data-url="%s" data-counter="right"></script></div>' % self.url
        if self.plus is True:
            htm += '<div class="socbut"><div size="standard" class="g-plusone" data-href="%s"  data-size="medium" data-annotation="bubble" count="true"></div></div>' % self.url
        return htm

