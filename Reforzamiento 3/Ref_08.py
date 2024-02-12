class Alumno:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.edad = input("Ingrese su edad: ")

    def imprimir(self):
        x = {}
        x['nombre'] = self.nombre
        x['apellido'] = self.apellido
        x['edad'] = self.edad
        print("Los datos completos del alumno son: " + self.nombre + " " + self.apellido + " " + "y tiene " + self.edad + " años")

alumno = Alumno()
alumno.imprimir()
