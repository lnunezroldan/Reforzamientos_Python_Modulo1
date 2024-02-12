class Ejemplo:
    def __init__(self, numero):
        self.numero = numero

    def cubo(self):
        print(int(self.numero) ** 3)

    def cuadrado(self):
        print(int(self.numero) ** 2)

ejemplo = Ejemplo(int(input("Ingrese un número entero: ")))
ejemplo.cubo()
ejemplo.cuadrado()