import unittest

import nose.tools as n

import pluplusch.cli as cli

class TestArgParser(unittest.TestCase):
    p = cli.arg_parser()
    def test_empty(self):
        parsed = self.p.parse_args([])
        n.assert_true(parsed.urls)
        n.assert_false(parsed.download_data)
        n.assert_contains('.pluplusch', p.cache_dir)
        n.assert_list_equal(p.catalogs, [])
