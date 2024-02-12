numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

def cuadrado (a):
    return a ** 2

m = []
for x in range(numero1, numero2):
    m.append(cuadrado(x))

print("Los cuadrados de los números ingresados son: {}".format(m))