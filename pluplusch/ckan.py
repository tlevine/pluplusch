import json
import functools, itertools
from urllib.parse import urljoin

import requests
from pickle_warehouse import Warehouse

def dataset_ids(get, catalog, page):
    url = urljoin(catalog, '/api/search/dataset?q=&start=%d' % page)
    response = get(url)
    data = json.loads(response.text)
    return data['results']

def dataset(get, catalog, datasetid):
    url = urljoin(catalog, '/api/rest/dataset/%s' % datasetid)
    response = get(url)
    dataset = json.loads(response.text)
    dataset['catalog'] = catalog
    return dataset

def download(get, warehouse, catalog):
    dataset_ids_page = functools.partial(dataset_ids, get, catalog)
    for page in itertools.count(1):
        result = dataset_ids_page(page)
        if result == []:
            break
        else:
            for dataset_id in result:
                yield dataset(get, catalog, dataset_id)
