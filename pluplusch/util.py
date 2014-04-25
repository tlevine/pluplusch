from pickle_warehouse import Warehouse
from picklecache import downloader

get = downloader(lambda url: requests.get(url), Warehouse('.pluplusch', mutable = False))
