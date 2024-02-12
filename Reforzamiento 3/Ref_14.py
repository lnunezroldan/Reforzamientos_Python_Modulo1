class Persona:
    def __init__(self):
        self.nombre = input("Ingresar nombres: ")
        self.apellido = input("Ingresar apellidos: ")
        self.edad = input("Ingresar edad: ")

    def seguro(self):
        input("Ingrese el tipo de seguro que tiene: ")

class Asociado(Persona):
    def estado(self):
        if int(self.edad) >= 18:
            print("Es MAYOR de edad")
        else:
            print("Es MENOR de edad")

aso1 = Asociado()
aso1.seguro()
aso1.estado()