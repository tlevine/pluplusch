import unittest

import nose.tools as n

import pluplusch.cli as cli

class TestArgParser(unittest.TestCase):
    p = cli.arg_parser()
    def test_empty(self):
        parsed = self.p.parse_args([])
        n.assert_false(parsed.urls)
        n.assert_false(parsed.download_data)
        n.assert_in('.pluplusch', parsed.cache_dir)
        n.assert_list_equal(parsed.catalog, [])
    def test_store_true(self):
        parsed = self.p.parse_args(['--url', '--download-data'])
        n.assert_true(parsed.urls)
        n.assert_true(parsed.download_data)

    def test_cache_dir(self):
        parsed = self.p.parse_args(['--cache-dir', 'foo'])
        n.assert_equal('foo', parsed.cache_dir)

    def test_catalogs(self):
        parsed = self.p.parse_args(['a','b','c'])
        n.assert_list_equal(parsed.catalog, ['a','b','c'])
