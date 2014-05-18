import os, json
import datetime
from collections import namedtuple

import nose.tools as n

import pluplusch.socrata as socrata

def test_views_page():
    catalog = 'https://foo.bar'
    Response = namedtuple('Response', ['text'])
    observed = socrata.views_page(lambda _: Response('[{"abc":"def"}]'), catalog, 1)
    n.assert_list_equal(observed, [{'abc':'def','catalog':'https://foo.bar',}])

def test_standardize_t6ck_kg3u():
    with open(os.path.join('pluplusch', 'test', 'fixtures', 't6ck-kg3u.json'), 'r') as fp:
        original = json.load(fp)
    observed = socrata.standardize(original)
    expected = {
        'url': 'https://healthmeasures.aspe.hhs.gov/d/t6ck-kg3u',
        'download_url': 'https://healthmeasures.aspe.hhs.gov/resource/t6ck-kg3u.csv',
        "title": "Measure Overviews",
        "creator_name" : "Erin Miller",
        "creator_id": "https://healthmeasures.aspe.hhs.gov/d/dg59-t3xw",
        "date": datetime.datetime(2014, 4, 9, 20, 39, 43),
        "tags" : {"measures"},
        "colnames": set(),
    }
    n.assert_dict_equal(observed, expected)

def test_standardize_zt9s_n5aj():
    with open(os.path.join('pluplusch', 'test', 'fixtures', 'zt9s-n5aj.json'), 'r') as fp:
        original = json.load(fp)
    observed = socrata.standardize(original)
    expected = {
    }
    n.assert_dict_equal(observed, expected)
