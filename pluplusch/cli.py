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
    parser.add_argument('--download-data', '-D', action = 'store_true', default = True)
    parser.add_argument('--urls', '-u', action = 'store_true', default = True)
    parser.add_argument('catalog', metavar = 'CATALOG', nargs = '*')

    return parser

def main(stdout = sys.stdout):
    p = arg_parser()
    p.parse_args()

    generator = pluplusch(catalogs = p.catalog, cache_dir = p.cache_dir, standardize = True, download_data = p.download_data)
    for dataset in generator:
        if p.url:
            url = metadata['download_url']
            stdout.write(url + '\n')
        else:
            stdout.write(json.dumps(metadata) + '\n')
