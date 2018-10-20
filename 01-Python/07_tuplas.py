tupla = (1, 2, 3, 2, 3, 3, "a", "b", "c")
print(tupla)
for numero in tupla:
    print(f"Numero: {numero}")
print(tupla.index(3)) # Devuelve el indice del valor
print(tupla.count(2))
print(tupla[0:2])
print(set(tupla))
for t in set(tupla):
    print(f"Valor: {t}")