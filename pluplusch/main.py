import os
from concurrent.futures import ThreadPoolExecutor
import logging

from pickle_warehouse import Warehouse
from picklecache import cache
import requests

import pluplusch.index as i
 
def getlogger():
    logger = logging.getLogger(__name__)
    fp_stream = logging.StreamHandler()
    fp_stream.setLevel(logging.ERROR)
    logger.addHandler(fp_stream)
    return logger
logger = getlogger()

def pluplusch(catalogs = None,
        cache_dir = os.path.join(os.path.expanduser('~'), '.pluplusch'),
        proxies = {}, standardize = False):
    '''
    pluplusch downloads data from open data websites. Here are
    its inputs.

    catalogs
        List of catalogs do download, each item being either
        a full URL string, including the scheme, or a tuple
        of the full URL string and the software, in case pluplusch
        doesn't know about the catalog
    cache_dir
        String directory to cache downloads to
    proxies
        A dictionary containing any or neither of "http_proxy"
        and "https_proxy"
    standardize
        Should the metadata be reduced and standardized across data
        catalog softwares (True), or should they be kept as is (False)?

    It returns a generator of datasets.
    '''

    @cache(cache_dir, mutable = False)
    def _get(url):
        return requests.get(url, proxies = proxies, verify = False)
    def get(url):
        try:
            response = _get(url)
        except Exception as e:
            logger.error('Could not download ' + url)
            logger.error(e)
            raise e
        if response.ok:
            return response
        else:
            raise ValueError('%d response at %s' % (response.status_code, url))

    if catalogs == None:
        # Use all catalogs.
        catalogs = list(i.all_catalogs())

    def dataset_generator(catalog_name, catalog_software, submodules = i.submodules()):
        for dataset in submodules[catalog_software].metadata(get, catalog_name):
            if standardize:
                yield submodules[catalog_software].standardize(get, dataset)
            else:
                yield dataset

    catalog_names = ((catalog[0] if len(catalog) == 2 else catalog) for catalog in catalogs)
    catalog_softwares = ((catalog[1] if len(catalog) == 2 else i.catalog_to_software(catalog)) for catalog in catalogs)
    standardized_catalogs = zip(catalog_names, catalog_softwares)
    generators = {catalog_name:dataset_generator(catalog_name, catalog_software) for catalog_name, catalog_software in standardized_catalogs}

    with ThreadPoolExecutor(len(generators)) as e:
        from time import sleep
        queue = []
        futures = {}
        while generators != {}:
            sleep(0.01)

            # Emit results.
            yield from queue
            queue.clear()

            # Start jobs.
            for catalog_name, generator in generators.items():
                if catalog_name not in futures:
                    futures[catalog_name] = e.submit(next, generator)

            # Enqueue results.
            for catalog_name, future in list(futures.items()):
                if future.done():
                    del(futures[catalog_name])
                    if future.exception() == None:
                        queue.append(future.result())
                    elif isinstance(future.exception(), StopIteration):
                        del(generators[catalog_name])
                    else:
                        del(generators[catalog_name])
                        logger.error('Error on ' + catalog_name)
                        logger.error(future.exception())
