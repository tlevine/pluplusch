from collections import namedtuple

import nose.tools as n

import pluplusch.ckan as ckan

Response = namedtuple('Response', ['text'])

def test_dataset_ids():
    fake_get = lambda _: Response('{"results":[{"a":3}]}')
    observed = ckan.dataset_ids(fake_get, 'https://foo-catalog.sh', 2)
    n.assert_list_equal(observed, [{'a': 3}])

def test_dataset():
    fake_get = lambda _: Response('{}')
    observed = ckan.dataset(fake_get, 'bar-catalog', 'whatever')
    n.assert_dict_equal(observed, {'catalog': 'bar-catalog'})

def test_standardize():
    original = {
        "license_title": null,
        "maintainer": "Ernesto Batista da Silva Filho",
        "maintainer_email": "ernesto.silva-filho@planejamento.gov.br",
        "id": "b0a6f2b2-26c5-454e-a0b7-0ce26b6f735a",
        "metadata_created": "2013-12-03T14:38:48.896740",
        "relationships": [],
        "license": null,
        "metadata_modified": "2013-12-03T14:38:48.896740",
        "author": "Ernesto Batista da Silva Filho",
        "author_email": "ernesto.silva-filho@planejamento.gov.br",
        "download_url": "http://www.visualizador.inde.gov.br/VisualizaCamada/92",
        "state": "active",
        "version": null,
        "license_id": null,
        "type": null,
        "resources": [
            {
                "resource_group_id": "dafa045c-f307-4487-8b40-68c074d2effd",
                "cache_last_updated": null,
                "package_id": "b0a6f2b2-26c5-454e-a0b7-0ce26b6f735a",
                "webstore_last_updated": null,
                "id": "a20d8867-f28c-4af6-931b-f5e94ad72afe",
                "size": null,
                "last_modified": null,
                "hash": "",
                "description": "Programa 2075",
                "format": "text/html",
                "tracking_summary": {"total": 0,
                "recent": 0},
                "mimetype_inner": null,
                "mimetype": null,
                "cache_url": null,
                "name": null,
                "created": "2013-12-03T12:38:48.942146",
                "url": "http://www.visualizador.inde.gov.br/VisualizaCamada/92",
                "webstore_url": null,
                "position": 0,
                "resource_type": null
            }, {
                "resource_group_id": "dafa045c-f307-4487-8b40-68c074d2effd",
                "cache_last_updated": null,
                "package_id": "b0a6f2b2-26c5-454e-a0b7-0ce26b6f735a",
                "webstore_last_updated": null,
                "id": "5d1069d1-07da-4cd5-a02a-883613a230bd",
                "size": null,
                "last_modified": null,
                "hash": "",
                "description": "Programa 2075",
                "format": "xml",
                "tracking_summary": {"total": 0,
                "recent": 0},
                "mimetype_inner": null,
                "mimetype": null,
                "cache_url": null,
                "name": null,
                "created": "2013-12-03T12:38:48.942169",
                "url": "http://www.geoservicos.inde.gov.br/geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=MPOG:Transporte_Rodoviario_Acesso&width=1024&height=768&bbox=-74,-34,-29,6",
                "webstore_url": null,
                "position": 1,
                "resource_type": null
            }
        ],
        "tags": ["INDE"],
        "tracking_summary": {
            "total": 0,
            "recent": 0
        },
        "groups": [],
        "name": "adequacao-de-acesso-rodoviario",
        "isopen": false,
        "notes_rendered": "<p>Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio. Empreendimentos pertencentes a carteira do Anexo III do PPA 2012-2015. Programa 2075. Iniciativas 00AL e 00AM - escala 1:2.500.000. Sistema de refer\u00eancia: SIRGAS2000.\n</p>",
        "url": "http://www.metadados.inde.gov.br/geonetwork/srv/br/metadata.show?uuid=670968af-9bfa-4a29-b77e-2b7a8871db23&currTab=simple",
        "ckan_url": "http://dados.gov.br//dataset/adequacao-de-acesso-rodoviario",
        "notes": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio. Empreendimentos pertencentes a carteira do Anexo III do PPA 2012-2015. Programa 2075. Iniciativas 00AL e 00AM - escala 1:2.500.000. Sistema de refer\u00eancia: SIRGAS2000.",
        "title": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio",
        "ratings_average": null,
        "extras": {"\u00d3rg\u00e3o - Poder": "Executivo",
        "\u00d3rg\u00e3o - Esfera": "Federal"},
        "ratings_count": 0,
        "revision_id": "a355ad23-6fe9-4217-a893-522417e73cd9"
    }
    observed = ckan.standardize(original)
    expected = {
        "maintainer": "Ernesto Batista da Silva Filho",
        "maintainer_email": "ernesto.silva-filho@planejamento.gov.br",
        "metadata_created": "2013-12-03T14:38:48.896740",
        "license": null,
        "metadata_modified": "2013-12-03T14:38:48.896740",
        "author": "Ernesto Batista da Silva Filho",
        "author_email": "ernesto.silva-filho@planejamento.gov.br",
        "tags": {"INDE"},
        "url": "http://dados.gov.br//dataset/adequacao-de-acesso-rodoviario",
        "notes": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio. Empreendimentos pertencentes a carteira do Anexo III do PPA 2012-2015. Programa 2075. Iniciativas 00AL e 00AM - escala 1:2.500.000. Sistema de refer\u00eancia: SIRGAS2000.",
        "title": "Adequa\u00e7\u00e3o de acesso rodovi\u00e1rio",
    }
