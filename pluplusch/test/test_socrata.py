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
    original = {
        'catalog': 'https://healthmeasures.aspe.hhs.gov',

        "id" : "t6ck-kg3u",
        "name" : "Measure Overviews",
        "averageRating" : 0,
        "createdAt" : 1325616190,
        "displayType" : "table",
        "downloadCount" : 37,
        "indexUpdatedAt" : 1397175791,
        "newBackend" : False,
        "numberOfComments" : 0,
        "oid" : 7728928,
        "publicationAppendEnabled" : False,
        "publicationDate" : 1397075983,
        "publicationGroup" : 268458,
        "publicationStage" : "published",
        "rowsUpdatedAt" : 1397075953,
        "rowsUpdatedBy" : "iwgp-sfie",
        "tableId" : 1540716,
        "totalTimesRated" : 0,
        "viewCount" : 643,
        "viewLastModified" : 1397075983,
        "viewType" : "tabular",
        "grants" : [ {
          "inherited" : True,
          "type" : "viewer",
          "flags" : [ "public" ]
        } ],
        "metadata" : {
          "renderTypeConfig" : {
            "visible" : {
              "page" : True,
              "table" : True
            },
            "active" : {
              "page" : {
                "id" : "40"
              }
            }
          },
          "availableDisplayTypes" : [ "table", "fatrow", "page" ]
        },
        "owner" : {
          "id" : "dg59-t3xw",
          "displayName" : "Erin Miller",
          "screenName" : "Erin Miller"
        },
        "rights" : [ "read" ],
        "tableAuthor" : {
          "id" : "dg59-t3xw",
          "displayName" : "Erin Miller",
          "screenName" : "Erin Miller"
        },
        "tags" : [ "measures" ],
        "flags" : [ "default" ]
    }
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
