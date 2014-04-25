from collections import namedtuple

import nose.tools as n

import pluplusch.ckan as ckan

Response = namedtuple('Response', ['text'])

def test_dataset_ids():
    fake_get = lambda _: Response('{"results":[{"a":3}]}')
    observed = ckan.dataset_ids(fake_get, 'https://foo-catalog.sh', 2)
    n.assert_list_equal(observed, [{'a': 3}])

def test_dataset():
    fake_get = lambda _: Response('{}')
    observed = ckan.dataset(fake_get, 'bar-catalog', 'whatever')
    n.assert_dict_equal(observed, {'catalog': 'bar-catalog'})
