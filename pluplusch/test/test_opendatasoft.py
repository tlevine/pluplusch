import datetime
from collections import namedtuple

import nose.tools as n

import pluplusch.opendatasoft as ods

Response = namedtuple('Response', ['text','ok'])

def test_datasets():
    def get(url):
        return Response(text = '{"datasets":[{"foo":8}]}', ok = True)
    catalog = 'stnoheustahoe'

    observed = ods.datasets(get, catalog)
    expected = [{'foo':8,'catalog':catalog}]
    n.assert_list_equal(observed, expected)

def test_standardize():
    original = {
        "datasetid": "liste-des-espaces-de-retrait-so-colissimo-sans-horaires",
        "catalog": "http://data.iledefrance.fr",
        "has_records": True,
        "features": [
          "analyze",
          "geo"
        ],
        "metas": {
          "records_count": 1029,
          "publisher": "La poste",
          "language": "fr",
          "title": "Liste des espaces de retrait So Colissimo (sans horaires)",
          "modified": "2014-03-12T16:46:09+00:00",
          "visibility": "domain",
          "description": "<p>Ce jeu de donn\u00e9es repr\u00e9sente l'ensemble des points de contact \u00e9ligibles au service So Colissimo, hors points relais Pick Up et espaces Courrier.</p><p>Il comporte le r\u00e9f\u00e9rentiel des points : identifiant, nom, adresse, coordonn\u00e9es g\u00e9ographiques (WGS) , un indicateur d\u2019accessibilit\u00e9 aux personnes \u00e0 mobilit\u00e9 r\u00e9duites, et le type de point relais :&nbsp;</p><p>- BPR = bureau de Poste relais&nbsp;</p><p>- CIT = Cityssimo</p><p> - ACP = Agence Coliposte</p>",
          "domain": "datailedefrance",
          "references": "http://www.data.gouv.fr/fr/dataset/liste-des-espaces-de-retrait-so-colissi-0",
          "theme": "Vie urbaine",
          "license": "Licence Ouverte",
          "keyword": [
            "R\u00e9seau postal",
            "Courrier",
            "G\u00e9olocalisation"
          ]
        },
        "attachments": [],
        "fields": [
            {
              "label": "Ident_pr",
              "name": "ident_pr",
              "type": "int"
            },
            {
              "label": "Nom_Point_de_retrait",
              "name": "nom_point_de_retrait",
              "type": "text"
            },
            {
              "label": "Adresse 1",
              "name": "adresse_1",
              "type": "text"
            },
            {
              "label": "Adresse 2",
              "name": "adresse_2",
              "type": "text"
            },
            {
              "label": "Adresse 3",
              "name": "adresse_3",
              "type": "text"
            },
            {
              "label": "Adresse 4",
              "name": "adresse_4",
              "type": "text"
            },
            {
              "label": "Code_postal",
              "name": "code_postal",
              "type": "int",
              "annotations": [
                {
                  "name": "facet"
                }
              ]
            },
            {
              "label": "Code_departement",
              "name": "code_departement",
              "type": "int",
              "annotations": [
                {
                  "name": "facet"
                }
              ]
            },
            {
              "label": "Ville",
              "name": "ville",
              "type": "text",
              "annotations": [
                {
                  "name": "facet"
                }
              ]
            },
            {
              "label": "Accessibilit\u00e9 perssonnes \u00e0 mobilit\u00e9 r\u00e9duite",
              "name": "accessibilite_perssonnes_a_mobilite_reduite",
              "type": "int",
              "annotations": [
                {
                  "name": "facet"
                }
              ]
            },
            {
              "label": "Type",
              "name": "type",
              "type": "text",
              "annotations": [
                {
                  "name": "facet"
                }
              ]
            },
            {
              "label": "wgs84",
              "name": "wgs84",
              "type": "geo_point_2d"
            }
        ]
    }
    observed = ods.standardize(original)
    expected = {
        "url": "http://data.iledefrance.fr/explore/dataset/liste-des-espaces-de-retrait-so-colissimo-sans-horaires",
        "title": "Liste des espaces de retrait So Colissimo (sans horaires)",
        "creator_name": "La poste",
        "creator_id": None,
        "date":  datetime.datetime(2014, 3, 12, 16, 46, 9),
        "tags" : {"R\u00e9seau postal", "Courrier", "G\u00e9olocalisation"},
        "colnames": {'type', 'wgs84', 'accessibilite_perssonnes_a_mobilite_reduite', 'ident_pr', 'code_postal', 'code_departement', 'adresse_2', 'adresse_3', 'nom_point_de_retrait', 'adresse_1', 'ville', 'adresse_4'},
    }
    n.assert_dict_equal(observed, expected)
