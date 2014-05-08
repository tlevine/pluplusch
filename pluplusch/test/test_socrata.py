import datetime
from collections import namedtuple

import nose.tools as n

import pluplusch.socrata as socrata

def test_page():
    Response = namedtuple('Response', ['text'])
    observed = socrata.page(lambda _: Response('[{}]'), 'https://foo.bar', 1)
    n.assert_list_equal(observed, [{}])

def test_standardize():
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
        "title": "Measure Overviews",
        "creator_name" : "Erin Miller",
        "creator_id": "https://healthmeasures.aspe.hhs.gov/d/dg59-t3xw",
        "date": datetime.datetime(2014, 4, 9, 20, 39, 43),
        "tags" : {"measures"},
    }
    n.assert_dict_equal(observed, expected)
