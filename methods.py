from data import methods, search_method

search = {clave: valor for claves, valor in search_method for clave in claves}


def get_method(type, metd):
    if type == "-s" and metd in search:
        return search.get(metd)
    elif type == "-m":
        return methods.get(metd)
    else:
        return f"No se encontró el método {metd}"
