# todo add init and update arguments, so we can call scaffold.builder init or update
import os, sys
import shutil
from scaffold.builder import docs
from scaffold.builder.minify import generate_static_content
from scaffold.builder import debian
from scaffold import web


def main(args=None):
    verbose = getattr(args, 'verbose', False)
    if 'init' == args.cmd:
        print('Creating new project')
        name = args.get('name') or 'example_project'
        path = args.get('path') or os.getcwd()
        root_path = path + os.sep + name + os.sep 

        if args.verbose is True:
            print("Creating new project %s" % path + os.sep + args.name + os.sep)
        
        folders = (
            '', 
            'site/', 
            'debian/', 
            'docs/', 
            'site/data/', 
            'site/data/sql', 
            'site/data/migrate', 
            'site/config/', 
            'site/views/', 
            'site/widgets/', 
            'site/static/css/', 
            'site/static/js/', 
            'site/static/images/',
            'site/static_resources/css/', 
            'site/static_resources/js/', 
            'site/static_resources/images/'
        )
        folders = [path + os.sep + name + os.sep + folder for folder in folders]
        for folder in folders:
            if os.path.exists(folder):
                continue
            os.makedirs(folder)
        debian.render(root_path + 'debian' + os.sep)

        # lets copy over some example files to get the user going
        template_folder = os.path.dirname(__file__) #os.path.abspath('./flask/')

        # example settings file
        shutil.copyfile(template_folder + '/flask/settings.py', root_path + 'site/config/settings.py')

        # example views 
        shutil.copyfile(template_folder + '/flask/index.py', root_path + 'site/index.py')
        shutil.copyfile(template_folder + '/flask/pages.py', root_path + 'site/views/pages.py')
        shutil.copyfile(template_folder + '/flask/profile_pages.py', root_path + 'site/views/profile_pages.py')

        # example data queries
        shutil.copyfile(template_folder + '/flask/profile_data.py', root_path + 'site/data/profile_data.py')
        shutil.copyfile(template_folder + '/flask/login_data.py', root_path + 'site/data/login_data.py')
        
        open(root_path + 'site/views/__init__.py', 'a').close()
        open(root_path + 'site/config/__init__.py', 'a').close()
        open(root_path + 'site/data/__init__.py', 'a').close()
        open(root_path + 'site/static/css/default.css', 'a').close()

        # copy info docs
        shutil.copyfile(template_folder + '/flask/static.md', root_path + 'site/static_resources/readme.md')

        web.auto_load_all()
        css = ''
        with open(root_path + 'site/static_resources/css/default.css', 'w') as default_css:
            css_fragments = [getattr(w, 'css', '') for w in web.widget() if getattr(w, 'css', '')]
            for css in css_fragments:
                if not os.path.exists(css):
                    continue 
                with open(css, 'r') as css_partial:
                    default_css.write(css_partial.read())
                    default_css.write("\n")
            #~ for w in web.widget():
                #~ print w
                #~ print web.elements[widget].__dict__.keys()
                #~ print getattr(widget, 'css', '')
                #~ css += getattr(widget, 'css', '')
                #~ css_fp.write(getattr(widget, 'css', ''))

    if 'update' in sys.argv:
        print('Updating project locate at %s' % os.path.abspath('../'))
        docs.render('API Docs', os.path.abspath('../'))

    if 'minify' in sys.argv:
        print('Optimising static content')
        source_path = getattr(args, 'path', os.path.abspath('./static_resources/'))
        target_path = getattr(args, 'path', os.path.abspath('./static/'))
        generate_static_content(source_path, target_path)
        

