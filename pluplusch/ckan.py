import json
import functools, itertools
from urllib.parse import urljoin

catalogs = [
    'datahub.io',
    'opendata.comune.bari.it',
    'africaopendata.org',
    'opendata.aragon.es',
    'daten.berlin.de',
    'data.buenosaires.gob.ar',
    'ie.ckan.net',
    'it.ckan.net',
    'rs.ckan.net',
    'br.ckan.net',
    'datos.codeandomexico.org',
    'cz.ckan.net',
    'dados.gov.br',
    'dadosabertos.senado.gov.br',
    'dados.novohamburgo.rs.gov.br',
    'data.gv.at',
    'data.linz.gv.at',
    'fi.thedatahub.org',
    'data.sa.gov.au',
    'www.data.gc.ca',
    'data.gov.sk',
    'data.gov.uk',
    'data.qld.gov.au',
    'data.openpolice.ru',
    'datacatalogs.org',
    'www.datagm.org.uk',
    'datakilder.no',
    'datospublicos.org',
    'data.denvergov.org',
    'ckan.emap.fgv.br',
    'open-data.europa.eu',
    'www.healthdata.gov',
    'www.hri.fi',
    'data.graz.gv.at',
    'daten.hamburg.de',
    'data.codeforhouston.com',
    'iatiregistry.org',
    'data.klp.org.in',
    'thedatahub.kr',
    'www.nosdonnees.fr',
    'offenedaten.de',
    'data.opencolorado.org',
    'catalog.opendata.in.th',
    'www.opendatahub.it',
    'dati.trentino.it',
    'data.openva.com',
    'www.opendata-hro.de',
    'opengov.es',
    'data.ottawa.ca',
    'data.overheid.nl',
    'www.opendata.provincia.roma.it',
    'publicdata.eu',
    'www.daten.rlp.de',
    'www.rotterdamopendata.nl',
    'data.cityofsantacruz.com',
    'thedatahub.org',
    'dati.toscana.it',
]

def dataset_ids(get, catalog, page):
    url = urljoin(catalog, '/api/search/dataset?q=&start=%d' % page)
    response = get(url)
    data = json.loads(response.text)
    return data['results']

def dataset(get, catalog, datasetid):
    url = urljoin(catalog, '/api/rest/dataset/%s' % datasetid)
    response = get(url)
    dataset = json.loads(response.text)
    dataset['catalog'] = catalog
    return dataset

def download(get, catalog):
    dataset_ids_page = functools.partial(dataset_ids, get, catalog)
    for page in itertools.count(1):
        result = dataset_ids_page(page)
        if result == []:
            break
        else:
            for dataset_id in result:
                yield dataset(get, catalog, dataset_id)
