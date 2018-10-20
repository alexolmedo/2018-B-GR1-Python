def hola_mundo():  # None
    print("Hola mundo")

print(hola_mundo())

def sumar_dos_numeros(num_uno, num_dos):
    if (num_uno == 1):
        return "Hola"
    else:
        return num_uno + num_dos

print(sumar_dos_numeros(3, 2))

def imprimir_universidad(nombre_universidad = "EPN"):
    print(f"{nombre_universidad} es lo máximo")

imprimir_universidad()

imprimir_universidad("Stanford")

def guardar_carros(posicion, placa, usuario, tip = None, color = None):
    print(f"Guardamos en {posicion} el auto con placa {placa}"
          f" del usuario {usuario}")
    if (color):
        print(f"El color del carro es {color}")
    if (tip):
        print(f"Se recibio un tip de {tip}")

guardar_carros(1,"ABC-123", "Alexander", 25.3, "Blue")

# normales
#  defecto or *

def sumar_numeros (resta, *numeros, valor_inicial=0 ):
    for numero in numeros:
        valor_inicial = valor_inicial + numero
    return valor_inicial - resta

resultado=sumar_numeros(1,1,2,3,4,5,6,7,8,4,valor_inicial=10)

print(resultado)

def imprimir_nombre(**kwargs):  ## Keyword arguments
    print(f"{kwargs['primer_nombre']} {kwargs['segundo_nombre']} {kwargs['apellido_paterno']} {kwargs['apellido_materno']}")

imprimir_nombre(primer_nombre="Alexander",
                segundo_nombre="Daniel",
                apellido_paterno="Olmedo",
                apellido_materno="Vinueza")

# numero=input("Ingrese un numero: ")

# print(float(numero) + 12.2 +1)

# opcional = input("Desea papas con su orden: ")
#
# if(True if opcional=="Si" else False):
#     print("Truthy")
# else:
#     print("Falsy")

# numeros = input("Ingrese numeros:\n")
# print(sumar_numeros(0,*list(map(float,numeros.split(","))),valor_inicial=0))

def calculadora(numero_uno, numero_dos, operacion="suma"):
    def sumar_dos_numeros():
        return numero_uno + numero_dos
    def restar_dos_numeros():
        return numero_uno - numero_dos
    def multiplicar_dos_numeros():
        return numero_uno * numero_dos
    def dividir_dos_numeros():
        return numero_uno / numero_dos

    def switch_operaciones():
        return {
            'suma': sumar_dos_numeros(),
            'resta': restar_dos_numeros(),
            'multiplicacion': multiplicar_dos_numeros(),
            "division": dividir_dos_numeros(),
        }[operacion]

    return switch_operaciones()

print(calculadora(1,2,'division'))
