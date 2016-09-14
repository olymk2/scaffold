from ...core.widget import base_widget


class control(base_widget):  
    link = None
    action = ""
    includes = []
    includes.append('<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>')

    comments = False
    share = True
    plus = True
    anotation = 'None'
    plus_one_size = 'medium'
    plus_one_annotation = 'inline'
    plus_one_comments_width = None

    def create(self, url, plus=True, share=False, comments=False):
        self.link = url
        self.plus = plus
        self.share = share
        self.comments = comments
        return self

    def url(self, link = None):
        self.link = link
        return self

    def render(self):
        link = ''
        self.count += 1
        htm = ''
        if self.link:
            link = ' data-href="' + self.link + '" '
        if self.plus is True:
            # <div class="g-plusone" data-size="medium" data-annotation="inline" data-width="300"></div>
            htm += '<div size="standard" class="g-plusone" ' + link + self.action + ' data-size="'+self.plus_one_size+'" data-annotation="'+self.plus_one_annotation+'" count="true"></div>'
        if self.share is True:
            htm += '<div class="g-plus" data-action="share" data-annotation="none"></div>'
        if self.comments is True:
            if self.plus_one_comments_width:
                width = ' data-width="%s"' % self.plus_one_comments_width
            htm += '<div class="g-comments" data-href="%s" data-first_party_property="BLOGGER" data-width="960" data-view_type="FILTERED_POSTMOD"></div>' % self.link
        return htm

