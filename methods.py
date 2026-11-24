from data import methods, search


def get_method(tip, metd):
    if tip not in ("-s", "-m"):
        return "Comando no válido, usar '-s' o '-m'"
    elif tip == "-s" and metd in search:
        return search.get(metd)
    elif tip == "-m" and metd in methods:
        return methods.get(metd)
    else:
        return "Metodo no encontrado"
