import os, json
import datetime
from collections import namedtuple

import nose.tools as n

import pluplusch.opendatasoft as ods

Response = namedtuple('Response', ['text','ok'])
def should_not_run(_):
    raise AssertionError('This should not run.')

def test_metadata():
    def get(url):
        return Response(text = '{"datasets":[{"foo":8}]}', ok = True)
    catalog = 'stnoheustahoe'

    observed = ods.metadata(get, catalog)
    expected = [{'foo':8,'catalog':catalog}]
    n.assert_list_equal(observed, expected)

def test_standardize_espaces_de_retrait():
    with open(os.path.join('pluplusch','test','fixtures','liste-des-espaces-de-retrait-so-colissimo-sans-horaires.json'), 'r') as fp:
        original = json.load(fp)
    observed = ods.standardize(original)
    expected = {
        "url": "http://data.iledefrance.fr/explore/dataset/liste-des-espaces-de-retrait-so-colissimo-sans-horaires",
        'download_url': 'http://data.iledefrance.fr/explore/dataset/liste-des-espaces-de-retrait-so-colissimo-sans-horaires/download/?format=csv' % original,
        "title": "Liste des espaces de retrait So Colissimo (sans horaires)",
        "creator_name": "La poste",
        "creator_id": None,
        "date":  datetime.datetime(2014, 3, 12, 16, 46, 9),
        "tags" : ["R\u00e9seau postal", "Courrier", "G\u00e9olocalisation"],
    }
    n.assert_dict_equal(observed, expected)
    observed_colnames = ods.colnames(should_not_run, original)
    expected_colnames = ['ident_pr', 'nom_point_de_retrait', 'adresse_1', 'adresse_2', 'adresse_3', 'adresse_4', 'code_postal', 'code_departement', 'ville', 'accessibilite_perssonnes_a_mobilite_reduite', 'type', 'wgs84']
    n.assert_list_equal(observed_colnames, expected_colnames)

def test_standardize_titles():
    with open(os.path.join('pluplusch','test','fixtures','les_1000_titres_les_plus_empruntes_2012_par_bibliotheque.json'), 'r') as fp:
        original = json.load(fp)
    observed = ods.standardize(original)
    expected = {
       'creator_id': None,
       'creator_name': None,
       'date': datetime.datetime(2013, 8, 7, 14, 59, 20),
       'download_url': 'http://opendata.paris.fr.opendatasoft.com/explore/dataset/les_1000_titres_les_plus_empruntes_2012_par_bibliotheque/download/?format=csv',
       'tags': ['bibliothèque', 'prêt', 'livres', 'statistiques'],
       'title': 'les 1000 titres les plus empruntés par bibliothèque en 2012',
       'url': 'http://opendata.paris.fr.opendatasoft.com/explore/dataset/les_1000_titres_les_plus_empruntes_2012_par_bibliotheque',
    }

    n.assert_dict_equal(observed, expected)
    observed_colnames = ods.colnames(should_not_run, original)
    expected_colnames = ['bibliotheque', 'rang', 'prets', 'type_de_document', 'titre', 'auteur']
    n.assert_list_equal(observed_colnames, expected_colnames)
