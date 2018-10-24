class Auto:
    pass


bm = Auto()

print(bm)


class Escuela:

    # valor_categoria = 4
    __ciudad = 'Quito'  # atributo privado
    pais = 'Ecuador'  # atributo publico

    def __init__(self, nombre, valor_categoria=4):
        print(self)
        print('Hola constructor')
        self.nombre = nombre
        self.valor_categoria = valor_categoria

    def saludar(self):
        print(f'Hola desde {self.nombre} localizada en'
              f' {self.__ciudad} - {self.pais}')

    def categoria(self):
        return self.__calcular_categoria()

    def __calcular_categoria(self):  # metodo privado
        return self.valor_categoria * 3

    def __str__(self):
        return 'Escuela'


# twa = Escuela('Theodoro Winword Anderson')
# twa.valor_categoria = 2
# twa.saludar()
# print(twa.categoria())

