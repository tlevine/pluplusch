from pickle_warehouse import Warehouse
from picklecache import downloader
import requests

import pluplusch.index as i
 
def pluplusch(catalogs = None, cache_dir = '.pluplusch', proxies = {}):

    _get = downloader(lambda url: requests.get(url, proxies = proxies), Warehouse(cache_dir, mutable = False))
    def get(url):
        response = _get(url)
        if response.ok:
            return response
        else:
            raise ValueError('%d response at %s' % (response.status_code, url))

    submodules = i.submodules()

    if catalogs == None:
        # Use all catalogs.
        catalogs = list(i.all_catalogs())

    generators = {catalog: getattr(submodules[i.catalog_to_software(catalog)], 'download')(get, catalog) for catalog in catalogs}
    while generators != {}:
        for catalog in list(generators.keys()):
            try:
                dataset = next(generators[catalog])
            except StopIteration:
                del(generators[catalog])
            else:
                yield dataset
