from concurrent.futures import ThreadPoolExecutor
from logging import getLogger

from pickle_warehouse import Warehouse
from picklecache import downloader
import requests

import pluplusch.index as i

logger = getLogger(__name__)
 
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
    def f(generator):
        try:
            result = next(generator)
        except StopIteration:
            result = None
        except Exception as e:
            result = None
            logger.error(e)
        return result

    while generators != {}:
        with ThreadPoolExecutor(len(generators)) as e:
            datasets = e.map(f, generators.values())
            remove = set()
            for catalog, dataset in zip(list(generators.keys()), datasets):
#               if dataset == None:
#                   remove.add(catalog)
#               else:
                    yield dataset
            for catalog in remove:
                del(generators[catalog])
