from pickle_warehouse import Warehouse
from picklecache import downloader

import pluplusch.index as i
 
def pluplusch(catalogs = None, cache_dir = '.pluplusch', proxies = {}):
    get = downloader(lambda url: requests.get(url, proxies = proxies), Warehouse(cache_dir, mutable = False))
    submodules = i.submodules()

    if catalogs == None:
        # Use all catalogs.
        catalogs = list(i.all_catalogs())

    for catalog in catalogs:
        software = i.catalog_to_software(catalog)
        yield from getattr(submodules[software], 'download')(get, catalog)
