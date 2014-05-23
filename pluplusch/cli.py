import os
import datetime
import argparse
import json
import sys

from pluplusch.main import pluplusch

def arg_parser():
    parser = argparse.ArgumentParser()

    cache_dir = os.path.expanduser('~/.pluplusch/' + datetime.date.today().isoformat())
    parser.add_argument('--cache-dir', '-d', metavar = 'DIR', default = cache_dir)
    parser.add_argument('--download-data', '-D', action = 'store_true', default = False)
    parser.add_argument('--urls', '-u', action = 'store_true', default = False)
    parser.add_argument('catalog', metavar = 'CATALOG', nargs = '*')

    return parser

def main(stdout = sys.stdout):
    p = arg_parser().parse_args()

    generator = pluplusch(catalogs = p.catalog, cache_dir = p.cache_dir, standardize = True, download_data = p.download_data)
    for metadata in generator:
        if p.urls:
            url = metadata['download_url']
            if url != None:
                stdout.write(url + '\n')
        else:
            for k,v in metadata.items():
                if isinstance(v, datetime.datetime):
                    metadata[k] = v.isoformat()
                elif isinstance(v, set):
                    metadata[k] = list(v)
            stdout.write(json.dumps(metadata) + '\n')
