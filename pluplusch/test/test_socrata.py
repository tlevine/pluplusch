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
    observed = socrata._standardize(True, original)
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
    observed = socrata._standardize(True, original)
    expected = {
        'url': 'https://data.cityofnewyork.us/d/zt9s-n5aj',
        'creator_id': 'https://healthmeasures.aspe.hhs.gov/d/5fuc-pqz2',
        'creator_name': 'NYC OpenData',
        'date': datetime.datetime(2014, 1, 24, 18, 20, 58),
        'download_url': 'https://data.cityofnewyork.us/resource/zt9s-n5aj.csv',
        'tags': {'lifelong learning'},
        'title': 'SAT (College Board) 2010 School Level Results',
        'colnames': {
            'dbn','school_name','number_of_test_takers',
            'critical_reading_mean', 'mathematics_mean', 'writing_mean',
        }
    }
    n.assert_dict_equal(observed, expected)
