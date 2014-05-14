from picklecache import cache

@cache(('pluplusch','test','fixtures','.pluplusch')):
def get_fromdisk(url):
    raise AssertionError('This function should never be called; the result should always come from the cache.')
