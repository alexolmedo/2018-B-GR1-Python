print("Hola Mundo")
edad: int = 20
sueldo: float = 1.02
print(edad + int(sueldo))
nombre = "Alexander"  # Comentario
apellido = 'Olmedo'
apellido_materno = """Vinueza"""
print(nombre == apellido)  # False
print(apellido == apellido_materno)  # False
print(apellido_materno)
print(int(True))  # 1
print(int(False))  # 0
print(str(True))  # "True"
print(str(False))  # "False"

print("alexander olmedo".capitalize())  # Alexander Olmedo
nombre_completo = "alexander olmedo".split(" ")  # ["alexander","olmedo"]
print(nombre_completo[0].capitalize() + " " + nombre_completo[1].capitalize())
print("Alexander".isalpha())  # True
print("Alexander10".isalpha())  # False
print("10".isnumeric())  # True
print("Alexander10".isnumeric())  # False
print("Alexander10".isalnum())  # True
print("10".isalnum())  # True
print("Mi nombre es {0} {1}".format(nombre_completo[0].capitalize(), "Olmedo"))
print(f"Mi nombre es {nombre_completo[0].capitalize()} {nombre_completo[1].capitalize()}")
print(r"Saltos de linea")  # raw
no_existo = None  # Null
print(no_existo)
