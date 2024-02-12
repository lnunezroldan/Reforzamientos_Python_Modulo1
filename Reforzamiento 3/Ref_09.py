import math

class Circulo:
    def __init__(self):
        self.radio = float(input("Ingrese el radio del circulo: "))

    def area(self):
        tipo = type(self.radio)
        if tipo == int or tipo == float:
            a = math.pi * (self.radio ** 2)
            print("El área del círculo es: {}".format(a))
        else:
            print("El valor ingresado no es de tipo numérico.")

    def perimetro(self):
        tipo = type(self.radio)
        if tipo == int or tipo == float:
            b = 2 * math.pi * self.radio
            print("El perímetro del círculo es: {}".format(b))
        else:
            print("El valor ingresado no es de tipo numérico.")

ins1 = Circulo()
ins1.area()
ins1.perimetro()

ins2 = Circulo()
ins2.area()
ins2.perimetro()