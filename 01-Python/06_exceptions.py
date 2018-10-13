adrian = {
    "nombre": "Adrian"
}
arregloNumeros = [1, 2]
try:
    arregloNumeros["1"] = 0
    asd = 21 + "a"
except (KeyError, TypeError) as errorQueSalte:  # For keys
    print(errorQueSalte)
except Exception as err:  # For keys
    print("Error in types")
    print(err.__traceback__)


"""
except TypeError as type:  # For keys
    print("Error in types")
    print(type)
    print(f"Linea del error: {type.__traceback__.tb_lineno}")
"""