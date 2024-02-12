class Persona:
    nombre = "nombre"
    edad = 0
    sueldo = 0
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def estado(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo: {self.sueldo}")

        n = int(self.edad)
        if n >= 18:
            print("Es MAYOR de edad")
        else:
            print("Es MENOR de edad")


    def bono(self):
        b = self.sueldo * 0.2
        print("Recibirá adionalmente {} soles de bono".format(b))

x = Persona("Luis", 33, 1500)
x.estado()
x.bono()
y = Persona("Javier", 29, 3000)
y.estado()
y.bono()
