import os
try:
    import slimit
    import cssmin
except:
    print('slimit or cssmin are not available')
from PIL import Image


image_list = {}


def generate_spritesheets(source_path, target_path):
    """generate spritesheets from same sized images"""
    target_image_path = target_path + 'images/sprites/'
    target_css_path = target_path + 'css/sprites/'
    if not os.path.exists(target_image_path):
        os.makedirs(target_image_path)
    if not os.path.exists(target_css_path):
        os.makedirs(target_css_path)

    spritesheet_count = 1
    spritesheet_size = 1024

    for size, images in image_list.items():
        pos_x, pos_y = 0, 0
        spritesheet = Image.new("RGBA", (1024, 1024), (0,0,0,0))
        spritesheet_name = 'sprites%s_%sx%sx' % (spritesheet_count, size, size)
        spritesheet_filename = '%s.png' % (spritesheet_name)
        spritesheet_csspath = '%s%s.css' % (target_css_path, spritesheet_name)
        spritesheet_imagepath = '%s%s' % (target_image_path, spritesheet_filename)

        with open(spritesheet_csspath, 'w') as css_fp:
            css_fp.write(".%s {background-image: url('%s');}\n" % (spritesheet_name, spritesheet_csspath))
            for image in images:
                name = os.path.splitext(os.path.basename(image))[0]
                if pos_x + size > spritesheet_size:
                    pos_x = 0
                    pos_y += size
                    
                tile = Image.open(image)
                box = (pos_x, pos_y, pos_x + size, pos_y + size)
                spritesheet.paste(tile, box)
                tile.close()
                
                pos_x += size
                css_fp.write('.%s{width:%s;height:%s;background-position:%s %s;}\n' % (name, size,  size, pos_x, pos_y))
            spritesheet.save(
                spritesheet_imagepath, 
                optimize=True, 
                quality=85)
    
    
def minify_image(filename, source_path, target_path):
    """optimize images"""
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    img = Image.open(source_path + os.sep + filename)
    width, height = img.size
    if width == height:
        image_list.setdefault(width, []).append(source_path + os.sep + filename)
    img.save(target_path + os.sep + filename, optimize=True, quality=85)

def minify_css(filename, source_path, target_path):
    """shrink the css file"""
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    with open(target_path + os.sep + filename, 'w') as target_fp:
        with open(source_path + os.sep + filename, 'r') as source_fp:
            target_fp.write(
                cssmin.cssmin(source_fp.read())
            )    

def minify_js(filename, source_path, target_path):
    """shrink the javascript file"""
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    with open(target_path + os.sep + filename, 'w') as target_fp:
        with open(source_path + os.sep + filename, 'r') as source_fp:
            target_fp.write(
                slimit.minify(source_fp.read(), mangle=True, mangle_toplevel=True)
            )    

def walk_files(path, target_folder, extensions=('.png', '.jpg', '.css', '.js')):
    """walk over the source directory and return the filename sorurce and destination folders"""
    for root, dirs, files in os.walk(path):
        relative_path = root[len(path):]
        for filename in files:
            if filename.endswith(extensions):
                yield filename, root, target_folder + relative_path


def generate_static_content(source_folder, target_folder='/tmp/static/'):
    """start the minification process, converts css js and images"""
    if not os.path.exists(source_folder):
        print('Source path %s does not exist' % source_folder)
        return 
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename, source_filename, target_filename in walk_files(source_folder, target_folder):
        if filename.endswith('.css'):
            minify_css(filename, source_filename, target_filename)
        
        if filename.endswith('.js'):
            minify_js(filename, source_filename, target_filename)
        
        if filename.endswith('.png'):
            minify_image(filename, source_filename, target_filename)
        
        if filename.endswith('.jpg'):
            minify_image(filename, source_filename, target_filename)

    #generate_spritesheets(source_filename, target_folder)


if __name__ == '__main__':
    generate_static_content(os.path.abspath('../../') + os.sep)
