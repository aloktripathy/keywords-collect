def keyword_occurences(filename):
    '''
    Takes a file and gives back the list of keywords in it alongwith their frequency of occurences
    filename -- string
    '''
    
    import re
    import ignore
    
    txt = read_file(filename)
    #do a case insensitive match
    txt = txt.lower()
    if txt is None:
        return None
    
    pattern = r'[\w]+'
    raw_keywords_list = re.findall(pattern, txt)
    raw_keywords_count = len(raw_keywords_list)
    raw_keywords_set = set(raw_keywords_list)
    raw_keywords_set_cardinality = len(raw_keywords_set)
    keywords_set = raw_keywords_set.difference(ignore.words)
    keywords_set_cardinality = len(keywords_set)
    keywords_count = sum( [raw_keywords_list.count(keyword) for keyword in keywords_set] )
    
    keywords_dict = [ {'keyword' : keyword, 'frequency' : raw_keywords_list.count(keyword), 'percentage' : str((raw_keywords_list.count(keyword) / keywords_count) * 100) + '%'} for keyword in keywords_set ]
    
    report = {
        'number of keywords' : keywords_count,
        'number of unique keywords' : keywords_set_cardinality,
        'noise' : str( keywords_count/raw_keywords_count * 100) + '%',
        'keywords' : sorted(keywords_dict, key=lambda keyword:keyword['frequency'], reverse=True)
    }
    return report


def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
        f.close()
    except IOError:
        print('invalid filename or file does not exist')
        return None
    

def write_file(filename, data):
    try:
        f = open(filename, 'w')
        f.write(data)
        f.close()
    except IOError:
        print('invalid filename or file does not exist')
        return None