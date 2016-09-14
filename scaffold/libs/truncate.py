
def paragraph(content, length=100, suffix='...'):
    """shorten text with out cuting of mid word"""
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix
