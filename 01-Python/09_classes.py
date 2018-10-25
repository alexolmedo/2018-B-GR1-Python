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


twa = Escuela('Theodoro Winword Anderson')
twa.valor_categoria = 2
twa.saludar()
print(twa.categoria())


class Auto:
    _ensamblado = 'Quito'
    numero_asientos = 5

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __init__(self, nombre, color, color_techo=''):
        self.nombre = nombre
        self.color = color
        self.color_techo = color_techo

    def cambiar_ensamblado(self, ensamblado):
        self._ensamblado = ensamblado

    def __maximo_numero_pasajeros(self):
        return self.numero_asientos + 3

    def __str__(self):
        return (f"{self.nombre}\n"
                f"{self.color}\n"
                f"{self.color_techo}\n"
                f"{self.numero_asientos}\n"
                f"{self._ensamblado}\n"
                f"{self.__maximo_numero_pasajeros()}\n")


bmw = Auto('Blanco', 'Version 1')
print(bmw)


class Hyundai(Auto):

    def __init__(self, color, nombre):
        super().__init__(color=color, nombre=nombre)
        print('constructor')
        print(self._ensamblado)


mi_carro = Hyundai('Negro', 'Santa fe')
print(mi_carro)