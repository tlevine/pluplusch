from collections import namedtuple

import nose.tools as n

import pluplusch.socrata as socrata

def test_page():
    Response = namedtuple('Response', ['text'])
    observed = socrata.page(lambda _: Response('[{}]'), 'https://foo.bar', 1)
    n.assert_list_equal(observed, [{}])
