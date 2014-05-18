import datetime
from collections import namedtuple

import nose.tools as n
n.assert_dict_equal.__self__.maxDiff = None

import pluplusch.ckan as ckan

Response = namedtuple('Response', ['text'])

def test_search():
    fake_get = lambda _: Response('{"results":[{"a":3}]}')
    observed = ckan.search(fake_get, 'https://foo-catalog.sh', 2)
    n.assert_list_equal(observed, [{'a': 3}])

def test_rest():
    fake_get = lambda _: Response('{}')
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
        "tags": {"INDE"},
        "colnames": set(),
    }
    n.assert_dict_equal(observed, expected)

    original['resources'][-1]['format'] = 'csv'
    observed = ckan.standardize(original)
    expected = {
        "url": "http://dados.gov.br/dataset/adequacao-de-acesso-rodoviario",
        "download_url": "http://www.geoservicos.inde.gov.br/geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=MPOG:Transporte_Rodoviario_Acesso&width=1024&height=768&bbox=-74,-34,-29,6",
        "title": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio",
        "creator_name": "Ernesto Batista da Silva Filho",
        "creator_id": "ernesto.silva-filho@planejamento.gov.br",
        "date": datetime.datetime(2013, 12, 3, 14, 38, 48),
        "tags": {"INDE"},
        "colnames": set(),
    }
    n.assert_dict_equal(observed, expected)
