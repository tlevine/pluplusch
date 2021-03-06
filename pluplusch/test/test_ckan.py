from __future__ import unicode_literals

import datetime
import pickle, os
from collections import namedtuple

import nose.tools as n
n.assert_dict_equal.__self__.maxDiff = None

import pluplusch.ckan as ckan

Response = namedtuple('Response', ['text','ok'])

def should_not_run(_):
    raise AssertionError('This function should not be called.')

def test_search():
    fake_get = lambda _: Response('{"results":[{"a":3}]}', True)
    observed = ckan.search(fake_get, 'https://foo-catalog.sh', 2)
    n.assert_list_equal(observed, [{'a': 3}])

    with open(os.path.join('pluplusch', 'test', 'fixtures', 'dataset?q=&start=1'), 'rb') as fp:
        error, response = pickle.load(fp)
    fake_get = lambda _: response
    observed = ckan.search(fake_get, 'https://foo-catalog.sh', 1)
    expected = [
        '02031-bathy-5m-5-meter-bathymetric-contours-derived-from-data-collected-during-u-s-geological-',
        '02031-bathy-trk-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-bathymetry-trackli',
        '02031-chrp-500-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-shot-point-navigati',
        '02031-chrp-sol-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-seismic-navigation-s',
        '02031-chrpsht-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-shot-point-navigatio',
        '02031-chrptrk-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-chirp-seismic-trackl',
        '02031-sss-trk-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-sidescan-sonar-track',
        '02031-svp-geophysical-surveys-of-bear-lake-utah-idaho-september-2002-sound-velocity-profiles',
        '02trkln-boomer-seismic-reflection-trackline-data-for-usgs-cruise-00scc02',
        '04trkln-boomer-seismic-reflection-trackline-data-for-usgs-cruise-00scc04']
    n.assert_list_equal(observed, expected)

def test_rest():
    fake_get = lambda _: Response('{}', True)
    observed = ckan.rest(fake_get, 'bar-catalog', 'whatever')
    n.assert_dict_equal(observed, {'catalog': 'bar-catalog'})

def test_standardize():
    original = {
        "catalog": "http://dados.gov.br",

        "license_title": None,
        "maintainer": "Ernesto Batista da Silva Filho",
        "maintainer_email": "ernesto.silva-filho@planejamento.gov.br",
        "id": "b0a6f2b2-26c5-454e-a0b7-0ce26b6f735a",
        "metadata_created": "2013-12-03T14:38:48.896740",
        "relationships": [],
        "license": None,
        "metadata_modified": "2013-12-03T14:38:48.896740",
        "author": "Ernesto Batista da Silva Filho",
        "author_email": "ernesto.silva-filho@planejamento.gov.br",
        "download_url": "http://www.visualizador.inde.gov.br/VisualizaCamada/92",
        "state": "active",
        "version": None,
        "license_id": None,
        "type": None,
        "resources": [
            {
                "resource_group_id": "dafa045c-f307-4487-8b40-68c074d2effd",
                "cache_last_updated": None,
                "package_id": "b0a6f2b2-26c5-454e-a0b7-0ce26b6f735a",
                "webstore_last_updated": None,
                "id": "a20d8867-f28c-4af6-931b-f5e94ad72afe",
                "size": None,
                "last_modified": None,
                "hash": "",
                "description": "Programa 2075",
                "format": "text/html",
                "tracking_summary": {"total": 0,
                "recent": 0},
                "mimetype_inner": None,
                "mimetype": None,
                "cache_url": None,
                "name": None,
                "created": "2013-12-03T12:38:48.942146",
                "url": "http://www.visualizador.inde.gov.br/VisualizaCamada/92",
                "webstore_url": None,
                "position": 0,
                "resource_type": None
            }, {
                "resource_group_id": "dafa045c-f307-4487-8b40-68c074d2effd",
                "cache_last_updated": None,
                "package_id": "b0a6f2b2-26c5-454e-a0b7-0ce26b6f735a",
                "webstore_last_updated": None,
                "id": "5d1069d1-07da-4cd5-a02a-883613a230bd",
                "size": None,
                "last_modified": None,
                "hash": "",
                "description": "Programa 2075",
                "format": "xml",
                "tracking_summary": {"total": 0,
                "recent": 0},
                "mimetype_inner": None,
                "mimetype": None,
                "cache_url": None,
                "name": None,
                "created": "2013-12-03T12:38:48.942169",
                "url": "http://www.geoservicos.inde.gov.br/geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=MPOG:Transporte_Rodoviario_Acesso&width=1024&height=768&bbox=-74,-34,-29,6",
                "webstore_url": None,
                "position": 1,
                "resource_type": None
            }
        ],
        "tags": ["INDE"],
        "tracking_summary": {
            "total": 0,
            "recent": 0
        },
        "groups": [],
        "name": "adequacao-de-acesso-rodoviario",
        "isopen": False,
        "notes_rendered": "<p>Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio. Empreendimentos pertencentes a carteira do Anexo III do PPA 2012-2015. Programa 2075. Iniciativas 00AL e 00AM - escala 1:2.500.000. Sistema de refer\u00eancia: SIRGAS2000.\n</p>",
        "url": "http://www.metadados.inde.gov.br/geonetwork/srv/br/metadata.show?uuid=670968af-9bfa-4a29-b77e-2b7a8871db23&currTab=simple",
        "ckan_url": "http://dados.gov.br//dataset/adequacao-de-acesso-rodoviario",
        "notes": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio. Empreendimentos pertencentes a carteira do Anexo III do PPA 2012-2015. Programa 2075. Iniciativas 00AL e 00AM - escala 1:2.500.000. Sistema de refer\u00eancia: SIRGAS2000.",
        "title": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio",
        "ratings_average": None,
        "extras": {"\u00d3rg\u00e3o - Poder": "Executivo",
        "\u00d3rg\u00e3o - Esfera": "Federal"},
        "ratings_count": 0,
        "revision_id": "a355ad23-6fe9-4217-a893-522417e73cd9"
    }
    observed = ckan.standardize(original)
    expected = {
        "url": "http://dados.gov.br/dataset/adequacao-de-acesso-rodoviario",
        "download_url": None,
        "title": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio",
        "creator_name": "Ernesto Batista da Silva Filho",
        "creator_id": "ernesto.silva-filho@planejamento.gov.br",
        "date": datetime.datetime(2013, 12, 3, 14, 38, 48),
        "tags": ["INDE"],
    }
    n.assert_dict_equal(observed, expected)

    original['resources'][-1]['format'] = 'csv'
    fake_get = lambda url: Response('peanut.butter,jelly\r\n', True)
    observed = ckan.standardize(original)
    expected = {
        "url": "http://dados.gov.br/dataset/adequacao-de-acesso-rodoviario",
        "download_url": "http://www.geoservicos.inde.gov.br/geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=MPOG:Transporte_Rodoviario_Acesso&width=1024&height=768&bbox=-74,-34,-29,6",
        "title": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio",
        "creator_name": "Ernesto Batista da Silva Filho",
        "creator_id": "ernesto.silva-filho@planejamento.gov.br",
        "date": datetime.datetime(2013, 12, 3, 14, 38, 48),
        "tags": ["INDE"],
    }
    n.assert_dict_equal(observed, expected)
    observed_colnames = ckan.colnames(fake_get, original)
    expected_colnames = ['peanut.butter','jelly']
    n.assert_list_equal(observed_colnames, expected_colnames)
