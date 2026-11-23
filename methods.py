from data import methods, search_method

search = {clave: valor for claves, valor in search_method for clave in claves}


def get_method(tip, metd):
    if tip not in ("-s", "-m"):
        return "Comando no válido, usar '-s' o '-m'"
    elif tip == "-s" and metd in search:
        return search.get(metd)
    elif tip == "-m" and metd in methods:
        return methods.get(metd)
    else:
        return "Metodo no encontrado"
