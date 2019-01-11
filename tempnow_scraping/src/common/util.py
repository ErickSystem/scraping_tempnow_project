import re

def format_cityname(txt):
    '''

    '''
    from unicodedata import normalize
    t = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    t = t.replace(" ", "")
    return str(t).lower()

def convert_by_int(txt):
    '''

    '''
    pattern_int = re.compile(r"(0|-?[1-9][0-9]*)")
    if pattern_int.match(txt):
        return int(txt)
    else:
        return 0
