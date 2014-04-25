softwares = ['azavea','ckan','junar','opendatasoft','socrata']

def submodules(softwares):
    return {software: __import__('pluplush.%s' % software) for software in softwares}

def catalogs(submodules):
    for software, module in submodules.items():
        for catalog in getattr(module, 'catalogs'):
            yield catalog, software

def catalog_to_software(catalog, lookup = {}):
    if lookup == {}:
        lookup.update(catalogs(submodules(softwares)))

    if catalog in lookup:
        return lookup[catalog]
    else:
        if catalog.startswith('http'):
            msg = "I don't know the software that this catalog uses."
        else:
            msg = "I don't know this catalog; try adding \"http://\" in front of the URL."
        raise msg

def all_catalogs():
    for catalog, software in catalogs(submodules(softwares)):
        yield catalog
