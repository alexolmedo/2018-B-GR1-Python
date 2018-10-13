arregloNumero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in arregloNumero:
    print(numero)

for indice in range(1, 5):
    print(f"Numero de iteracion: {indice}")

for indice in range(3):
    print(f"Numero de iteracion: {indice}")

for indice in range(7, 10):
    print(f"Numero de iteracion: {indice}")

for indice in range(10):
    print(f"Numero de iteracion: {indice}")
    if (indice == 6):
        break  # Detener la ejecucion del loop

for indice in range(10):
    if (indice == 6 or indice == 4):
        continue  # Detener la ejecucion de esta iteracion, el loop continua
    print(f"Numero de iteracion: {indice}")

numeroAuxiliar = 0
while numeroAuxiliar < 10:
    print(f"Numero: {numeroAuxiliar}")
    numeroAuxiliar += 1

numeroAuxiliarDos = 0
while True:
    print(f"Numero: {numeroAuxiliarDos}")
    numeroAuxiliarDos += 1
    if numeroAuxiliarDos == 70:
        break
