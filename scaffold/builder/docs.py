import os
import token
import tokenize
from io import StringIO
from scaffold import web

# TODO use built in breadcrumbs
def breadcrumbs(full_path, crumbs):
    htm = '' if len(crumbs) < 1 else '<a href="%sindex_new.htm">Home</a>\n' % (full_path)
    path = '' 
    for crumb in crumbs[0:-1]:
        if crumb:
            path += crumb + '/'
            htm += '<a href="%s%sindex_new.htm">%s</a>\n' % (full_path, path,  crumb.title())
    return htm
        
def build_docs_folder_tree(root_path, output_folder, exclude=[]):
    """Scan the source tree, and create the same directory structure inside the docs folder
        Args:
            root_path = root folder to scan and reproduce the folders
            output_folder = folder to place the docs
            exclude = folders to skip
    """
    if not os.path.exists(output_folder):
        os.mkdir(output_folder) 

    for root, dirs, files in os.walk(root_path):
        relative_path = root.replace(root_path, '').strip(os.sep)
        if relative_path.startswith(tuple(exclude)):
            continue

        for dirpath in dirs:
            relative_folder = relative_path + os.sep + dirpath
            if not os.path.exists(output_folder + relative_folder):
                os.mkdir(output_folder + relative_folder)


def get_files(root_path, exclude=[]):
    """Scan the source tree, return py files and there relative paths, 
    skip files that start with __ or do not start with .py
        Args:
            root_path = root folder to scan and reproduce the folders
            exclude = folders to skip
    """
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            if filename.startswith('__') or not filename.endswith('.py'):
                continue
            current_file_path = root + os.sep + filename
            relative_path = root.replace(root_path, '').lstrip(os.sep)
            filename = os.path.split(current_file_path)[-1]
            relative_folders = []
            if relative_path:
                relative_folders = relative_path.strip(os.sep).split(os.sep)
            
            for folder in relative_folders:
                if folder in exclude or folder.startswith('__'):
                    break
            else:
                yield relative_folders, filename


def build_relative_path(root, path):
    return path.replace(root, '').lstrip(os.sep)


def build_relative_path_list(root, path):
    return build_relative_path(root, path).split(os.sep)


class parse_source_code:
    splitter = ['args:', 'links:', 'images:', 'returns:']
    htm = StringIO()

    def title(self, text):
        raise NotImplemented

    def list_header(self, text, url):
         raise NotImplemented

    def link(self, url, link):
         raise NotImplemented

    def __init__(self, relative_path, source_file): # , destination_file
        """ Run on just one file."""
        source = open(source_file)
        token_generator = tokenize.generate_tokens(source.readline)

        #with formatter(destination_file) as page:
        path, filename = os.path.split(source_file)
        path = path[len(os.path.abspath('../')):]
        self.header(filename[0:-3])

        prev_token_type = token.INDENT
        prev_token_text = ''
        last_lineno = -1
        last_col = 0
        
        web.container.create()
        for token_type, ttext, (slineno, scol), (elineno, ecol), ltext in token_generator:
            if 0:   # Change to if 1 to see the tokens fly by.
                print(tokenize.tok_name.get(token_type, token_type))
                print("%10s %-14s %-20r %r" % (
                    tokenize.tok_name.get(token_type, token_type),
                    "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                    ttext, ltext
                    ))
            if slineno > last_lineno:
                last_col = 0

            if token_type == token.NAME and prev_token_text in ('class', 'def'):
                title = ltext.lstrip("\t")[len(prev_token_text):]
                web.container.append(
                    web.title.create(title).render()
                )
                #self.title(ltext.lstrip("\t")[len(prev_token_text):] + "\n")
            #~ if token_type == token.NAME and prev_token_text == 'def':
                #~ self.title(ltext.lstrip("\t")[4:] + "\n")
            if token_type == token.STRING and prev_token_type == token.INDENT:
                web.container.append(
                    web.title.create(ttext.strip('"""')).render()
                )
                #~ self.paragraph("\t" + ttext.strip('"""') + "\n")
                self.paragraph(web.container.render())
            if token_type == tokenize.COMMENT:
                continue

            prev_token_type = token_type
            prev_token_text = ttext
            last_col = ecol
            last_lineno = elineno


class generate_index:
    indent = 0
    previous_folder = ''

    def __init__(self):
        self.htm = StringIO("<ul>")

    def header(self, text):
        raise NotImplemented

    def list_header(self, text, url):
         raise NotImplemented

    def __enter__(self):
        self.htm.write("<ul>")
        return self
    
    def __exit__(self, type, value, traceback):
        self.htm.write('</ul>')

    def tabs(self, offset=0):
        return "  " * (self.indent + offset)

    def append(self, relative_path, text):
        #check if path has changed 
        if len(relative_path) and relative_path[-1] != self.previous_folder:

            # depth decreased
            if len(relative_path) <= self.indent:
                for pos in range(len(relative_path), self.indent + 1):
                    self.htm.write("\n%s</ul></li>" % self.tabs())
                    self.indent -= 1
            
            # depth increased
            if len(relative_path) >= self.indent:
                for pos in range(self.indent, len(relative_path)):
                    self.indent += 1
                    self.htm.write("\n%s<li>%s<ul>" % (self.tabs(), self.index_link(relative_path[pos], relative_path)))
            
            # remember the last folder, we may go up a level and back down a level so we need to check for that
            self.previous_folder = relative_path[-1]

        # output the node at the current depth
        self.indent = len(relative_path)
        self.htm.write("\n%s<li>%s</li>" % (self.tabs(1), self.page_link(text, relative_path)))

    def read(self):
        for pos in range(0, self.indent):
            self.indent -= 1
            self.htm.write("\n%s</ul>" % self.tabs())
        self.htm.seek(0)
        return self.htm.read()


class formatter_default:
    index_close = 0
    splitter = ['args:', 'links:', 'images:', 'returns:']

    def url(self, relative_path):
        return "/".join(relative_path)

    def __enter__(self):
        self.htm.write("<ul>")
        return self
    
    def __exit__(self, type, value, traceback):
        self.htm.write('</ul>')

    def read(self):
        self.htm.seek(0)
        return self.htm.read()

    def header(self, text):
        web.page.create(web.title.create(text).render())

    def list_header(self, text, url):
        return '<h2 class="expander"><a href="%s">%s</a></h2>'

    def index_link(self, title, link, indent=1):
        return web.link.create(
            title=title,
            content=title,
            link="%s/index_new.htm" % "/".join(link)
        ).render()

    def page_link(self, title, link, indent=1):
        return web.link.create(
            title=title,
            content=title,
            link="%s/%s.htm" % ('/'.join(link), title[0:-3])
        ).render()

    # TODO use built in breadcrumbs
    def breadcrumbs(self, full_path, crumbs):
        htm = '' if len(crumbs) < 1 else '<a href="%sindex_new.htm">Home</a>\n' % (full_path)
        path = '' 
        for crumb in crumbs[0:-1]:
            if crumb:
                path += crumb + '/'
                htm += '<a href="%s%sindex_new.htm">%s</a>\n' % (full_path, path,  crumb.title())
        return htm

    def title(self, text):
        self.fp.write(('<h3 class="expander" >%s</h3>\n' % text.strip()))

    def paragraph(self, text):
        self.content(text)
        #self.fp.write("<p>%s</p>\n\n" % text)
    
    def content(self, format_text):
        indent = 0
        for text in format_text.split("\n"):
            text=text.strip()
            if text.lower() in self.splitter:
                if indent > 0:
                    self.fp.write('</ul></div>')
                    indent -= 1
                self.fp.write('<div style="margin-left:' + str((indent+1)*40)+ 'px;"><h4>%s</h4><ul>' % text)
                indent += 1
            else:
                if indent == 0:
                    self.fp.write('<div style="margin-left:' + str((indent+1)*40)+ 'px;" >%s</div>' % text)
                else:
                    if text:
                        self.fp.write(indent * "\t" + '<li>%s</li>' % text)
                
        if indent > 0:
            self.fp.write('</ul></div>')


class index_fomatter(generate_index, formatter_default):
    pass
    #~ def header(self, text):
        #~ web.page.create(text)
        #~ #self.fp.write(("<h2>%s</h2>\n" % text.strip()))

    #~ def list_header(self, text, url):
        #~ return '<h2 class="expander"><a href="/%s_index.htm">%s</a></h2>' % ("/".join(url), text)


class page_formatter(parse_source_code, formatter_default):

    def breadcrumbs(self, full_path, crumbs):
        path = full_path
        for crumb in crumbs:
            if crumb:
                path += crumb + os.sep
                return self.htm.write('<a href="%s%s.htm">%s</a>\n' % (path, crumb, crumb))

    def title(self, text):
        return self.htm.write(web.title.create(text).render())

    def header(self, text):
        return self.htm.write(web.title.create(text).render())
        #self.fp.write(("<h2>%s</h2>\n" % text.strip()))

    def paragraph(self, text):
        self.content(text)
        #self.fp.write("<p>%s</p>\n\n" % text)
    
    def content(self, format_text):
        indent = 0
        for text in format_text.split("\n"):
            text = text.strip()
            if text.lower() in self.splitter:
                if indent > 0:
                    self.htm.write('</ul></div>')
                    indent -= 1
                self.htm.write('<div style="margin-left:' + str((indent + 1) * 40) + 'px;"><h4>%s</h4><ul>' % text)
                indent += 1
            else:
                if indent == 0:
                    self.htm.write('<div style="margin-left:' + str((indent + 1) * 40) + 'px;" >%s</div>' % text)
                else:
                    if text:
                        self.htm.write(indent * "\t" + '<li>%s</li>' % text)
                
        if indent > 0:
            self.htm.write('</ul></div>')

def generate_main_index(root_path, index_path, relative_path, ignore_folders, output_root_folder):
    # generate index
    title = root_path.split(os.sep)[-1]
    relative_path_list = build_relative_path_list(root_path, index_path)
    output_folder = output_root_folder + os.sep + os.sep.join(relative_path) + os.sep
    with index_fomatter() as index:
        for relative_folders, filename in get_files(index_path, ignore_folders):
            print(filename)
            index.append(relative_folders, filename)
        #print output_folder + 'index_new.htm'
        with open(output_folder + 'index_new.htm', 'w') as main_index:
            web.page.create("Index %s" % title)
            web.page.section(index.breadcrumbs(output_root_folder, relative_path_list))
            web.page.section(index.read())
            web.template.append(web.page.render())
            main_index.write(web.render())

def generate_pages(domain, root_path, ignore_folders, output_folder):
    #~ relative_path, 
    for relative_folders, filename in get_files(root_path, ignore_folders):
        relative_folders.append(filename)
        source_file = "%s/%s" % (root_path, "/".join(relative_folders))
        destination_file = "%s%s.htm" % (output_folder, "/".join(relative_folders)[0:-3])
        with page_formatter(relative_folders, source_file) as page:
            with open(destination_file, 'w') as html_page:
                web.page.create(relative_folders[-1])
                
                web.breadcrumbs.create(domain)
                relative_folders[-1] = relative_folders[-1] + 'index_new.htm'
                web.breadcrumbs * relative_folders
                web.page.section(web.breadcrumbs.render())

                web.page.section(page.read())
                web.template.append(web.page.render())
                html_page.write(web.render())

def generate_docs(domain, project_name, root_path, output_folder, exclude_extend=['.bzr', '.git', '.svn', '__pycache__']):
    """ Generate documentation for python file located in supplied path
    
        Args:
            root_path: Read python project from this folder
            output_folder: store results in this location
            formatter: custom class to format the output
    """

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    ignore_folders = ['docs', 'images', 'tests', '.bzr', '.git', 'dev', 'models', '__pycache__']
    build_docs_folder_tree(root_path, output_folder, ignore_folders)

    #generate_main_index(root_path, ignore_folders, output_folder)
    for relative_folders, filename in get_files(root_path, ignore_folders):
        index_root = root_path + os.sep + os.sep.join(relative_folders)
        index_output_folder = output_folder + os.sep.join(relative_folders) + os.sep
        generate_main_index(
            root_path=root_path,
            index_path=index_root,
            relative_path=relative_folders,
            ignore_folders=ignore_folders,
            output_root_folder=output_folder)
    
    generate_pages(domain, root_path, ignore_folders, output_folder)

        
def render(name, root_path, domain=None):
    
    output_folder = root_path + ('/docs/api') + os.sep
    domain = 'file:///' + output_folder
    generate_docs(domain, name, root_path, output_folder)
    
if __name__ == '__main__':
    render('API Docs', os.path.abspath('../../'))
