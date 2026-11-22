campos = [
    (["name", "nombre"], "yerson"),
    (["age", "edad"], 18),
    (["city", "ciudad"], "Lima"),
]

persona = {clave: valor for claves, valor in campos for clave in claves}

print(persona.get("name"))    # yerson
print(persona.get("nombre"))  # yerson

print(persona.get("age"))     # 18
print(persona.get("edad"))    # 18
