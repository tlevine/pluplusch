from __future__ import unicode_literals

import os, json
import datetime
from collections import namedtuple

import nose.tools as n

import pluplusch.socrata as socrata

try:
    UTC = datetime.timezone.utc
except AttributeError:
    UTC = None # Dates will be interpreted in local time on Python 2.

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
        u'url': u'https://healthmeasures.aspe.hhs.gov/d/t6ck-kg3u',
        u'download_url': u'https://healthmeasures.aspe.hhs.gov/resource/t6ck-kg3u.csv',
        u'title': u'Measure Overviews',
        u'creator_name': u'Erin Miller',
        u'creator_id': u'https://healthmeasures.aspe.hhs.gov/d/dg59-t3xw',
        u'date': datetime.datetime(2014, 4, 9, 20, 39, 43, tzinfo = UTC),
        u'tags': {u'measures'},
    }
    n.assert_dict_equal(observed, expected)

def test_standardize_zt9s_n5aj():
    with open(os.path.join('pluplusch', 'test', 'fixtures', 'zt9s-n5aj.json'), 'r') as fp:
        original = json.load(fp)
    observed = socrata.standardize(original)
    expected = {
        u'url': u'https://data.cityofnewyork.us/d/zt9s-n5aj',
        u'creator_id': u'https://healthmeasures.aspe.hhs.gov/d/5fuc-pqz2',
        u'creator_name': u'NYC OpenData',
        u'date': datetime.datetime(2014, 1, 24, 18, 20, 58, tzinfo = UTC),
        u'download_url': u'https://data.cityofnewyork.us/resource/zt9s-n5aj.csv',
        u'tags': {u'lifelong learning'},
        u'title': u'SAT (College Board) 2010 School Level Results',
    }
    n.assert_dict_equal(observed, expected)

    def fake_get(_):
        raise AssertionError('This should not run.')
    observed_colnames = socrata.colnames(fake_get, original)
    expected_colnames = [
        'dbn','school_name','number_of_test_takers',
        'critical_reading_mean', 'mathematics_mean', 'writing_mean',
    ]
    n.assert_list_equal(observed_colnames, expected_colnames)

def test_standardize_tags():
    origunal = {
        u'tableAuthor': {
            u'screenName': 'Clare',
            u'profileImageUrlSmall': u'/images/profile/2234/2577/180561_10150096076666249_317976_n_tiny.jpg',
            u'displayName': 'Clare',
            u'rights': [
                u'create_datasets',
                u'edit_others_datasets',
                u'edit_sdp',
                u'edit_site_theme',
                u'moderate_comments',
                u'manage_users',
                u'chown_datasets',
                u'edit_nominations',
                u'approve_nominations',
                u'feature_items',
                u'federations',
                u'manage_stories',
                u'manage_approval',
                u'change_configurations',
                u'view_domain',
                u'view_others_datasets',
                u'edit_pages',
                u'create_pages',
                u'view_goals',
                u'view_dashboards',
                u'edit_goals',
                u'edit_dashboards',
                u'create_dashboards'
            ],
            u'profileImageUrlMedium': '/images/profile/2234/2577/180561_10150096076666249_317976_n_thumb.jpg',
            u'profileImageUrlLarge': '/images/profile/2234/2577/180561_10150096076666249_317976_n_large.jpg',
            u'flags': ['admin'],
            u'id': 'rqdg-xj2v'
        },
        u'displayType': 'table',
        u'viewType': 'tabular',
        u'publicationGroup': 240034,
        u'newBackend': False,
        u'publicationDate': 1354232726,
        u'catalog': 'https://data.undp.org',
        u'rowsUpdatedBy': 'rqdg-xj2v',
        u'averageRating': 0,
        u'viewCount': 167,
        u'publicationStage': 'published',
        u'grants': [{'inherited': True,
        u'flags': ['public'],
        u'type': 'viewer'}],
        u'viewLastModified': 1319223058,
        u'rights': ['read'],
        u'oid': 1867464,
        u'numberOfComments': 0,
        u'rowsUpdatedAt': 1354232632,
        u'createdAt': 1319223058,
        u'publicationAppendEnabled': False,
        u'owner': {'screenName': 'UNDP Transparency',
        u'displayName': 'UNDP Transparency',
        u'id': '67n2-h4v3'},
        u'indexUpdatedAt': 1397848594,
        u'moderationStatus': True,
        u'downloadCount': 67,
        u'metadata': {'renderTypeConfig': {'visible': {'table': True}},
        u'custom_fields': {'Scope': {'Country': 'Bahamas'}},
        u'availableDisplayTypes': ['table',
        u'fatrow',
        u'page']},
        u'name': 'Projects in Bahamas',
        u'tableId': 527904,
        u'totalTimesRated': 0,
        u'id': 'mvag-axbk'
    }
    observed = socrata.standardize(original)
    expected = {
        'creator_id': 'https://healthmeasures.aspe.hhs.gov/d/67n2-h4v3',
        'creator_name': 'UNDP Transparency',
        'date': datetime.datetime(2012, 11, 29, 23, 45, 26, tzinfo = UTC),
        'download_url': 'https://data.undp.org/resource/mvag-axbk.csv',
        'tags': set(),
        'title': 'Projects in Bahamas',
        'url': 'https://data.undp.org/d/mvag-axbk',
    }
    n.assert_dict_equal(observed, expected)

def test_standardize_niuh_hrin():
    with open(os.path.join('pluplusch', 'test', 'fixtures', 'niuh-hrin.json'), 'r') as fp:
        original = json.load(fp)
    observed = socrata.standardize(original)
    expected = {
        'creator_id': 'https://healthmeasures.aspe.hhs.gov/d/5fuc-pqz2',
        'creator_name': 'NYC OpenData',
        'date': datetime.datetime(2014, 1, 8, 15, 37, 53, tzinfo = UTC),
        'download_url': None,
            # Or https://data.cityofnewyork.us/download/niuh-hrin/XLS ?
        'tags': set(),
        'title': 'Commuter Van Services - Vehicles',
        'url': 'https://data.cityofnewyork.us/d/niuh-hrin',
    }
    n.assert_dict_equal(observed, expected)
