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
    }
    n.assert_dict_equal(observed, expected)

def test_standardize_zt9s_n5aj():
    with open(os.path.join('pluplusch', 'test', 'fixtures', 'zt9s-n5aj.json'), 'r') as fp:
        original = json.load(fp)
    observed = socrata.standardize(original)
    expected = {
        'url': 'https://data.cityofnewyork.us/d/zt9s-n5aj',
        'creator_id': 'https://healthmeasures.aspe.hhs.gov/d/5fuc-pqz2',
        'creator_name': 'NYC OpenData',
        'date': datetime.datetime(2014, 1, 24, 18, 20, 58),
        'download_url': 'https://data.cityofnewyork.us/resource/zt9s-n5aj.csv',
        'tags': {'lifelong learning'},
        'title': 'SAT (College Board) 2010 School Level Results',
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
    original = {'tableAuthor': {'screenName': 'Clare', 'profileImageUrlSmall': '/images/profile/2234/2577/180561_10150096076666249_317976_n_tiny.jpg', 'displayName': 'Clare', 'rights': ['create_datasets', 'edit_others_datasets', 'edit_sdp', 'edit_site_theme', 'moderate_comments', 'manage_users', 'chown_datasets', 'edit_nominations', 'approve_nominations', 'feature_items', 'federations', 'manage_stories', 'manage_approval', 'change_configurations', 'view_domain', 'view_others_datasets', 'edit_pages', 'create_pages', 'view_goals', 'view_dashboards', 'edit_goals', 'edit_dashboards', 'create_dashboards'], 'profileImageUrlMedium': '/images/profile/2234/2577/180561_10150096076666249_317976_n_thumb.jpg', 'profileImageUrlLarge': '/images/profile/2234/2577/180561_10150096076666249_317976_n_large.jpg', 'flags': ['admin'], 'id': 'rqdg-xj2v'}, 'displayType': 'table', 'viewType': 'tabular', 'publicationGroup': 240034, 'newBackend': False, 'publicationDate': 1354232726, 'catalog': 'https://data.undp.org', 'rowsUpdatedBy': 'rqdg-xj2v', 'averageRating': 0, 'viewCount': 167, 'publicationStage': 'published', 'grants': [{'inherited': True, 'flags': ['public'], 'type': 'viewer'}], 'viewLastModified': 1319223058, 'rights': ['read'], 'oid': 1867464, 'numberOfComments': 0, 'rowsUpdatedAt': 1354232632, 'createdAt': 1319223058, 'publicationAppendEnabled': False, 'owner': {'screenName': 'UNDP Transparency', 'displayName': 'UNDP Transparency', 'id': '67n2-h4v3'}, 'indexUpdatedAt': 1397848594, 'moderationStatus': True, 'downloadCount': 67, 'metadata': {'renderTypeConfig': {'visible': {'table': True}}, 'custom_fields': {'Scope': {'Country': 'Bahamas'}}, 'availableDisplayTypes': ['table', 'fatrow', 'page']}, 'name': 'Projects in Bahamas', 'tableId': 527904, 'totalTimesRated': 0, 'id': 'mvag-axbk'}
    observed = socrata.standardize(original)
    expected = {
        'creator_id': 'https://healthmeasures.aspe.hhs.gov/d/67n2-h4v3',
        'creator_name': 'UNDP Transparency',
        'date': datetime.datetime(2012, 11, 29, 23, 45, 26),
        'download_url': 'https://data.undp.org/resource/mvag-axbk.csv',
        'tags': set(),
        'title': 'Projects in Bahamas',
        'url': 'https://data.undp.org/d/mvag-axbk',
    }
    n.assert_dict_equal(observed, expected)

@n.nottest
def test_standardize_niuh_hrin():
    with open(os.path.join('pluplusch', 'test', 'fixtures', 'niuh-hrin.json'), 'r') as fp:
        original = json.load(fp)
    observed = socrata.standardize(original)
    expected = {}
