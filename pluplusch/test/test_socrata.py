from collections import namedtuple

import nose.tools as n

import pluplusch.socrata as socrata

def test_page():
    Response = namedtuple('Response', ['text'])
    observed = socrata.page(lambda _: Response('[{}]'), 'https://foo.bar', 1)
    n.assert_list_equal(observed, [{}])

def test_standardize():
    original = {
        'catalog': https://healthmeasures.aspe.hhs.gov',

        "id" : "t6ck-kg3u",
        "name" : "Measure Overviews",
        "averageRating" : 0,
        "createdAt" : 1325616190,
        "displayType" : "table",
        "downloadCount" : 37,
        "indexUpdatedAt" : 1397175791,
        "newBackend" : false,
        "numberOfComments" : 0,
        "oid" : 7728928,
        "publicationAppendEnabled" : false,
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
          "inherited" : true,
          "type" : "viewer",
          "flags" : [ "public" ]
        } ],
        "metadata" : {
          "renderTypeConfig" : {
            "visible" : {
              "page" : true,
              "table" : true
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
    observed = socrata.standardize(json.loads(dataset_from_api))
    expected = {
        'url': 'https://healthmeasures.aspe.hhs.gov/d/t6ck-kg3u',
        "name": "Measure Overviews",
        "creator_name" : "Erin Miller"
        "creator_id": "https://healthmeasures.aspe.hhs.gov/d/dg59-t3xw",
        "date": None,
        "tags" : {"measures"},
    }
