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

def pluplusch(get, catalogs = None,
        cache_dir = os.path.join(os.path.expanduser('~'), '.pluplusch'))
    '''
    pluplusch downloads data from open data websites. Here are
    its inputs.

    catalogs
        List of catalogs to download, each item being either
        a full URL string, including the scheme, or a tuple
        of the full URL string and the software, in case pluplusch
        doesn't know about the catalog
    cache_dir
        String directory to cache downloads to

    It returns a generator of datasets.
    '''

    # Use all catalogs by default.
    if catalogs == None:
        catalogs = list(i.all_catalogs())

    # Detect catalog softwares if they're not specified.
    catalog_names = ((catalog[0] if len(catalog) == 2 else catalog) for catalog in catalogs)
    catalog_softwares = ((catalog[1] if len(catalog) == 2 else i.catalog_to_software(catalog)) for catalog in catalogs)
    catalog_names_softwares = zip(catalog_names, catalog_softwares)

    # Threading
    queue = []
    running = set(catalog_names)
    submodules = i.submodules()
    def enqueue_datasets(catalog_name_software):
        catalog_name, catalog_software = catalog_name_software
        for dataset in submodules[catalog_software].metadata(get, catalog_name):
            queue.append(dataset)
        running.remove(catalog_name)
    threaded(catalog_names_softwares, enqueue_datasets)
    while len(running) > 0:
        if queue != []:
            yield queue.pop(0)

def standardize(get, original, download_data = False, csv = False):


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
