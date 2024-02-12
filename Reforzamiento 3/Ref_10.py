class Alumno:
    nombre = "nombre"
    edad = 0
    nota = 0
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def estado(self):
        n = float(self.nota)
        if n >= 11:
            print("Su nota es {} y está APROBADO".format(self.nota))
        else:
            print("Su nota es {} y está DESAPROBADO".format(self.nota))

x = Alumno("Luis", 33, 15)
x.datos()
x.estado()
y = Alumno("Javier", 29, 10.4)
y.datos()
y.estado()
z = Alumno("Melissa", 30, 11)
z.datos()
z.estado()