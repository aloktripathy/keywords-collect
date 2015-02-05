def keyword_occurences(filename):
    '''
    Takes a file and gives back the list of keywords in it alongwith their frequency of occurences
    filename -- string
    '''
    
    import re
    import time
    import os
    import human_size
    import regex.pluralize
    
    import ignore
    
    timer = {}
    timer['total'] = -time.time()
    timer['reading_file'] = -time.time()
    txt = read_file(filename)
    timer['reading_file'] += time.time()
    #do a case insensitive match
    if txt == None:
        return None
    txt = txt.lower()
    timer['filesize'] = human_size.approximate_size(os.stat(filename).st_size)
    pattern = r'[\w]{2,}'
    timer['parsing'] = -time.time()
    timer['pattern_matching'] = -time.time()
    raw_keywords_list = re.findall(pattern, txt)
    timer['pattern_matching'] += time.time()
    
    raw_keywords_count = len(raw_keywords_list)
    keywords_list = []
    for word in raw_keywords_list:
        if(word not in ignore.words):
            keywords_list.append(word)    
    

    del raw_keywords_list
    keywords_set = set(keywords_list)
    keywords_set_cardinality = len(keywords_set)
    keywords_dict_list = [{'keyword' : keyword, 'frequency' : keywords_list.count(keyword)} for keyword in keywords_set]
    keywords_count = sum([keyword['frequency'] for keyword in keywords_dict_list])
    
    i = 0
    while i < keywords_set_cardinality:
        keywords_dict_list[i]['percentage'] = str((keywords_dict_list[i]['frequency'] / keywords_count) * 100) + '%'
        i += 1
    
    timer['parsing'] += time.time()
    timer['sorting_and_finalizing'] = -time.time()
    report = {
        'number of keywords' : keywords_count,
        'number of unique keywords' : keywords_set_cardinality,
        'noise' : str( keywords_count/raw_keywords_count * 100) + '%',
        'keywords' : keywords_dict_list.sort(key=lambda keyword:keyword['frequency'], reverse=True)
    }
    timer['sorting_and_finalizing'] += time.time()
    timer['total'] += time.time()
    timer['speed'] = str(os.stat(filename).st_size / timer['total']) + ' bytes/second'
    print(timer)
    return report


def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
        f.close()
    except :
        print('invalid filename or file does not exist')
        return None
    

def write_file(filename, data):
    try:
        f = open(filename, 'w')
        f.write(data)
        f.close()
    except:
        print('invalid filename or file does not exist')
        return None