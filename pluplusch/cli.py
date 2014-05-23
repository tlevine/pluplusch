import argparse

def arg_parser():
    parser = argparse.ArgumentParser()

    cache_dir = os.path.expanduser('~/.pluplusch/' + datetime.date.today().isoformat())
    parser.add_argument('--cache-dir', '-d', metavar = 'DIR', default = cache_dir)
    parser.add_argument('--download-data', '-D', action = 'store_true', default = True)
    parser.add_argument('--csv-urls', '-,', action = 'store_true', default = True)

    return parser

def generator_args(parsed_args):
    out = {}
    out['cache_dir'] = parsed_args.cache_dir
    if parsed_args.csv_urls:
        # pluplusch with csv flag on
        out['csv'] = True
    else:
        if parsed_args.download_data:
            # pluplusch with download_data flag on
            out['download_data'] = True
    return out
