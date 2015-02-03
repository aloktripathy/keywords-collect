SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
def approximate_size(size, format_1000 = True):
    '''Converts the size of a file to human readable format
    
    Keyword Arguments
    size -- file size in bytes
    format_1000 -- if True (default) then uses multiples of 1000
                -- else uses multiples of 1024
    Returns: string
    '''
    
    if not (isinstance(size, int) or isinstance(format_1000, bool)):
        raise ValueError('Function argument type mismatch')
    
    if size < 0:
        raise ValueError('Number must be non-negative')
    
    multiplier = 1000 if format_1000 else 1024
    for suffix in SUFFIXES[multiplier]:
        size /= multiplier
        if size < multiplier:
            return '{0:.1f}{1}'.format(size, suffix)