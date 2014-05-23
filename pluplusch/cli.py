import argparse
import json
import sys

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

    for nonstandard_metadata in pluplusch(catalogs = p.catalogs, cache_dir = p.cache_dir):
        if p.urls:
            url = download_url(nonstandard_metadata)
            stdout.write(url + '\n')
        else:
            standard_metadata = standardize(nonstandard_metadata, download_data = p.download_data)
            stdout.write(json.dumps(standard_metadata) + '\n')
