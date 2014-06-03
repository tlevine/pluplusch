from __future__ import unicode_literals

import unittest

import nose.tools as n

import pluplusch.cli as cli

class TestArgParser(unittest.TestCase):
    p = cli.arg_parser()
    def test_empty(self):
        parsed = self.p.parse_args([])
        n.assert_false(parsed.urls)
        n.assert_false(parsed.force_colnames)
        n.assert_false(parsed.silent)
        n.assert_in('.pluplusch', parsed.cache_dir)
        n.assert_list_equal(parsed.catalog, [])
    def test_store_true(self):
        parsed = self.p.parse_args(['--url', '--force-colnames'])
        n.assert_true(parsed.urls)
        n.assert_true(parsed.force_colnames)

    def test_cache_dir(self):
        parsed = self.p.parse_args(['--cache-dir', 'foo'])
        n.assert_equal('foo', parsed.cache_dir)

    def test_catalogs(self):
        parsed = self.p.parse_args(['a','b','c'])
        n.assert_list_equal(parsed.catalog, ['a','b','c'])
