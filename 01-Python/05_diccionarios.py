alexander = {
    'nombre': "Alexander",
    'apellido': 'Olmedo',
    "edad": 29,
    "sueldo": 10.1,
    "hijos": [],
    "casado": False,
    "loteria": None,
    "mascota": {
        "nombre": "Luli",
        "edad": 6
    }
}
print(alexander)
print(alexander["nombre"])
print(alexander["mascota"]["nombre"])
print(alexander.get("apellido"))
print(alexander.pop("casado"))
print(alexander)
print(alexander.values())

for valor in alexander.values():
    print(f"Valor: {valor}")

for key in alexander.keys():
    print(f"Llave: {key} Valor: {alexander.get(key)}")

for clave, valor in alexander.items():
    print(f"clave: {clave} valor: {valor}")

alexander["profesion"] = "Estudiante"

print(alexander)

nuevos_valores = {"peso": 170, "altura": 169}
alexander.update(nuevos_valores)
print(alexander)
