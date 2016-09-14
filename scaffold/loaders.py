import os


def load_resource(paths):
    with open(os.path.realpath(paths), 'r') as fp:
        return fp.read()

#~ realpath = os.path.realpath(_file_)
#~ dirname = os.path.dirname(realpath)
#~ joined = os.path.join(dirname, *paths)
#~ return joined


def load_partial(filepath, start=0, end=None):
    """ eturn the text between a start and stop line position """
    count = 0
    result = ''
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if count > start:
                    if end is None or count < end:
                        result += line
                count += 1
    return result


def load_partial_numbered(filepath, start=0, end=None):
    """ eturn the text between a start and stop line position """
    count = 0
    result = ''
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if count > start:
                    if end is None or count < end:
                        result  += str(count) + ' ' + line
                count += 1
    return result


def load_partial_lines(filepath, start=0, end=None):
    """ eturn the text between a start and stop line position """
    count = 0
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if count > start:
                    if end is None or count < end:
                        yield line
                count += 1


def load(filepath):
    """ return the contents of a file"""
    result = ''
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            result = f.read()
    return result


