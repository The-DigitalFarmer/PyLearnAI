# Cada nombre reúne una descripción con ejemplo y sus alias de búsqueda.
_catalog = {
    # Funciones y tipos
    "print": ("Imprimir en la terminal <print('Hola mundo')>", ("imprimir", "mostrar")),
    "input": ("Leer texto del usuario <input('Nombre: ')>", ("pedir", "solicitar")),
    "type": ("Consultar el tipo de un valor <type(42) => int>", ("tipo",)),
    "len": ("Contar elementos <len([1, 2]) => 2>", ("longitud", "cantidad")),
    "str": ("Convertir a texto <str(42) => '42'>", ("texto", "letra")),
    "int": ("Convertir a entero <int(1.2) => 1>", ("entero", "número", "numero")),
    "float": ("Convertir a número decimal <float('3.14') => 3.14>", ("decimal",)),
    "bool": ("Convertir a un valor lógico <bool([]) => False>", ("booleano",)),
    "list": ("Crear una lista <list('ab') => ['a', 'b']>", ("lista",)),
    "tuple": ("Crear una tupla <tuple([1, 2]) => (1, 2)>", ("tupla",)),
    "dict": ("Crear un diccionario <dict(edad=18) => {'edad': 18}>", ("diccionario",)),
    "set": ("Crear un conjunto <set([1, 1, 2]) => {1, 2}>", ("conjunto", "sin duplicados")),
    "range": ("Generar enteros hasta un límite excluido <list(range(1, 4)) => [1, 2, 3]>", ("generar", "secuencia")),
    "sum": ("Sumar los elementos de un iterable <sum([1, 2, 3]) => 6>", ("sumar",)),
    "max": ("Encontrar el valor mayor <max(1, 10) => 10>", ("máximo", "maximo")),
    "min": ("Encontrar el valor menor <min(1, 10) => 1>", ("mínimo", "minimo")),
    "abs": ("Calcular el valor absoluto <abs(-7) => 7>", ("valor absoluto",)),
    "round": ("Redondear un número <round(3.14159, 2) => 3.14>", ("redondear",)),
    "sorted": ("Obtener una nueva lista ordenada <sorted([3, 1, 2]) => [1, 2, 3]>", ("lista ordenada",)),
    "enumerate": ("Recorrer elementos con su índice <list(enumerate(['a', 'b'])) => [(0, 'a'), (1, 'b')]>", ("enumerar", "índice", "indice")),
    "zip": ("Combinar elementos de varios iterables <list(zip([1, 2], ['a', 'b'])) => [(1, 'a'), (2, 'b')]>", ("emparejar",)),
    "any": ("Comprobar si algún elemento es verdadero <any([False, True]) => True>", ("alguno",)),
    "all": ("Comprobar si todos los elementos son verdaderos <all([True, False]) => False>", ("todos",)),

    # Métodos de texto
    "lower": ("Convertir a minúsculas <'HOLA'.lower() => 'hola'>", ("minúscula", "minuscula")),
    "upper": ("Convertir a mayúsculas <'hola'.upper() => 'HOLA'>", ("mayúscula", "mayuscula")),
    "strip": ("Quitar espacios de los extremos <'  hola  '.strip() => 'hola'>", ("espacio", "sobrante")),
    "replace": ("Reemplazar texto <'hola mundo'.replace('mundo', 'Yerson') => 'hola Yerson'>", ("reemplazar", "cambiar")),
    "split": ("Dividir un texto por un separador <'a,b'.split(',') => ['a', 'b']>", ("separar",)),
    "join": ("Unir cadenas con un separador <'-'.join(['a', 'b']) => 'a-b'>", ("unir",)),
    "startswith": ("Comprobar el inicio de un texto <'hola'.startswith('ho') => True>", ("prefijo",)),
    "endswith": ("Comprobar el final de un texto <'foto.png'.endswith('.png') => True>", ("sufijo",)),
    "find": ("Encontrar la posición de un texto o devolver -1 <'hola'.find('la') => 2>", ("buscar texto",)),

    # Métodos de listas
    "append": ("Agregar un elemento al final <lista = [1, 2]; lista.append(3) deja [1, 2, 3]>", ("agregar", "añadir")),
    "pop": ("Eliminar y devolver un elemento por índice (el último por defecto) <[1, 2, 3].pop() => 3>", ("eliminar", "quitar")),
    "remove": ("Eliminar la primera aparición de un valor <lista = [1, 2, 2]; lista.remove(2) deja [1, 2]>", ("eliminar", "quitar")),
    "sort": ("Ordenar la lista en el lugar <lista = [3, 1, 2]; lista.sort() deja [1, 2, 3]>", ("ordenar",)),
    "extend": ("Agregar todos los elementos de un iterable <lista = [1]; lista.extend([2, 3]) deja [1, 2, 3]>", ("extender",)),
    "insert": ("Insertar en una posición <lista = [1, 3]; lista.insert(1, 2) deja [1, 2, 3]>", ("insertar",)),
    "count": ("Contar las apariciones de un valor <[1, 2, 2].count(2) => 2>", ("apariciones",)),
    "reverse": ("Invertir la lista en el lugar <lista = [1, 2, 3]; lista.reverse() deja [3, 2, 1]>", ("invertir",)),

    # Métodos de diccionarios
    "get": ("Buscar una clave con un valor por defecto <{}.get('edad', 0) => 0>", ("obtener", "valor por defecto")),
    "keys": ("Consultar las claves <list({'a': 1}.keys()) => ['a']>", ("claves",)),
    "values": ("Consultar los valores <list({'a': 1}.values()) => [1]>", ("valores",)),
    "items": ("Consultar los pares de clave y valor <list({'a': 1}.items()) => [('a', 1)]>", ("pares",)),
    "update": ("Agregar o reemplazar pares <datos = {'a': 1}; datos.update(a=2) deja {'a': 2}>", ("actualizar",)),

    # Métodos de conjuntos
    "add": ("Agregar un elemento a un conjunto <datos = {1}; datos.add(2) deja {1, 2}>", ("agregar al conjunto",)),
    "union": ("Obtener todos los elementos de dos conjuntos <{1, 2}.union({2, 3}) => {1, 2, 3}>", ("unión", "union")),
    "intersection": ("Obtener elementos en común <{1, 2}.intersection({2, 3}) => {2}>", ("intersección", "interseccion")),
    "difference": ("Obtener los elementos exclusivos del primer conjunto <{1, 2}.difference({2, 3}) => {1}>", ("diferencia",)),
}

methods = {name: description for name, (description, _) in _catalog.items()}

_suggestions_by_alias = {}
for name, (_, aliases) in _catalog.items():
    for alias in aliases:
        _suggestions_by_alias.setdefault(alias, []).append(f"{name}()")

search = {
    alias: " o ".join(suggestions)
    for alias, suggestions in _suggestions_by_alias.items()
}
