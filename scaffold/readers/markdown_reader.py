import os
from io import open
import misaka
from scaffold import web
from misaka import HtmlRenderer


class CustomRenderer(HtmlRenderer):
    def block_code(self, text, lang):
        return web.pre.create(text).render()


class markdown_reader:
    def __init__(self, markdown_file=None):
        renderer = CustomRenderer(misaka.HTML_USE_XHTML)
        self.md = misaka.Markdown(
            renderer,
            extensions=misaka.EXT_FENCED_CODE | misaka.EXT_NO_INTRA_EMPHASIS)
        if markdown_file is not None:
            self.create(markdown_file)

    def __call__(self):
        return self

    def create(self, markdown_file):
        self.markdown_file = markdown_file
        return self

    def render(self):
        if not os.path.exists(self.markdown_file):
            print('Markdown file does not exist')
        with open(self.markdown_file, encoding='UTF-8') as fp:
            #changed from .render to ()
            return self.md(fp.read())
