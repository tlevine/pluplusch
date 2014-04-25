catalogs = [
]

def download(get, catalog):
    raise NotImplementedError

def apikey(get, catalog, datetime):
    url = '%s/developer_manager/action_insert?_=%s' % (catalog, datetime.strftime('%s%f')[:-3])
    response = get(url)
    data = json.loads(response.text)
    return data['pApiKey']
