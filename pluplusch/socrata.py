import json
import functools
import itertools
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

catalogs = [
    'data.colorado.gov',
    'data.nola.gov',
    'healthmeasures.aspe.hhs.gov',
    'data.cityofchicago.org',
    'data.wa.gov',
    'opendata.go.ke',
    'data.austintexas.gov',
    'data.cityofnewyork.us',
    'info.samhsa.gov',
    'data.taxpayer.net',
    'data.cityofmadison.com',
    'data.slcgov.com',
    'data.illinois.gov',
    'data.somervillema.gov',
    'iranhumanrights.socrata.com',
    'data.hawaii.gov',
    'data.maryland.gov',
    'data.ny.gov',
    'data.mo.gov',
    'data.nfpa.org',
    'nmfs.socrata.com',
    'data.govloop.com',
    'data.sunlightlabs.com',
    'electionsdata.kingcounty.gov',
    'data.undp.org',
    'deleon.socrata.com',
    'data.energystar.gov',
    'explore.data.gov',
    'data.weatherfordtx.gov',
    'bronx.lehman.cuny.edu',
    'data.sfgov.org',
    'data.edmonton.ca',
    'data.consumerfinance.gov',
    'www.metrochicagodata.org',
    'data.kingcounty.gov',
    'data.baltimorecity.gov',
    'health.data.ny.gov',
    'dati.lombardia.it',
    'datacatalog.cookcountyil.gov',
    'www.opendatanyc.com',
    'cookcounty.socrata.com',
    'data.oregon.gov',
    'data.oaklandnet.com',
    'data.raleighnc.gov',
    'finances.worldbank.org',
    'data.honolulu.gov',
    'opendata.socrata.com',
    'data.cityofboston.gov',
    'data.ok.gov',
    'data.cms.gov',
    'data.snostat.org',
    'www.halifaxopendata.ca',
    'data.wellingtonfl.gov',
    'gettingpastgo.socrata.com',
    'www.data.act.gov.au',
    'data.redmond.gov',
    'data.seattle.gov',
    'data.montgomerycountymd.gov',
    'data.acgov.org',
    'data.medicare.gov'
]

def page(get, domain_with_scheme, page_number):
    full_url = urljoin(domain_with_scheme, '/api/views?page=%d' % page_number)
    response = get(full_url)
    search_results = json.loads(response.text)
    return search_results

def download(get, domain):
    for page_number in itertools.count(1):
        for search_results in functools.takewhile(lambda x: x != [], page(get, domain, page_number)):
            yield from search_results
