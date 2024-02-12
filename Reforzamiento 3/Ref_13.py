class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado (Persona):
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def impuesto(self):
        b = float(self.sueldo) * 0.1
        if float(self.sueldo) > 4000:
            print(f"Deberá pagar {b} soles de impuesto")
        else:
            print("No deberá pagar impuestos.")

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
sueldo = input("Ingrese su sueldo: ")

x = Empleado(nombre, edad, sueldo)
print(x.sueldo)
print(x.impuesto())