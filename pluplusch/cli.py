import os
import datetime
import argparse
import json
import sys

from pickle_warehouse import Warehouse
import pickle_warehouse.serializers as s

from pluplusch.main import pluplusch, get

def arg_parser():
    parser = argparse.ArgumentParser()

    cache_dir = os.path.join(os.path.expanduser('~'), '.pluplusch')
    parser.add_argument('--cache-dir', '-c', metavar = 'DIR', default = cache_dir,
        help = 'Use the specified directory as the cache directory; the default is "%s".' % cache_dir)
    parser.add_argument('--force-colnames', '-D', action = 'store_true', default = False,
        help = 'Set this flag to download full datasets when they are helpful, rather than relying on metadata files.')
    parser.add_argument('--urls', '-u', action = 'store_true', default = False,
        help = 'Display just the URLs of downloads rather than the full standardized metadata in jsonlines format.')
    parser.add_argument('catalog', metavar = 'CATALOG', nargs = '*',
        help = 'Manually specify catalogs; the default is to use lots of hard-coded catalogs.')

    parser.add_argument('--full', '-f', action = 'store_true', default = False,
        help = 'Download the full data files rather than just the metadata files.')

    parser.add_argument('--silent', '-s', action = 'store_true', default = False,
        help = 'Download stuff, but don\'t print anything to the screen.')

    parser.add_argument('--data-dir', '-d', metavar = 'DIR',
        help = 'Save dataset files to a directory (in addition to caching).')

    return parser

def main(stdout = sys.stdout, stderr = sys.stderr):
    p = arg_parser().parse_args()
    if p.silent:
        stdout = os.devnull

    generator = pluplusch(catalogs = p.catalog, standardize = True,
                          force_colnames = p.force_colnames,
                          get = lambda url: get(url, cache_dir = p.cache_dir))
    if p.data_dir != None:
        data_warehouse = Warehouse(p.data_dir, serializer = s.identity)
    for metadata in generator:
        if (p.full or p.data_dir != None) and metadata['download_url'] != None:
            try:
                response = get(metadata['download_url'])
            except:
                stderr.write('Skipping %s because of an error' % metadata['download_url'])
            if p.data_dir != None and response.ok and response.url not in data_warehouse:
                data_warehouse[response.url] = response.content
        if p.urls:
            url = metadata['download_url']
            if url != None:
                stdout.write(url + '\n')
                stdout.flush()
        else:
            for k,v in metadata.items():
                if isinstance(v, datetime.datetime):
                    metadata[k] = v.isoformat()
                elif isinstance(v, set):
                    metadata[k] = list(v)
            stdout.write(json.dumps(metadata) + '\n')
            stdout.flush()
