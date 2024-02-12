numero1 = int(input("Ingresar un número positivo: "))

"""Función de suma de dígitos"""
def sumdigits(a):
    suma = 0
    while a > 0:
        suma = suma + (a % 10)
        a = a // 10
    return suma

m = sumdigits(numero1)
print("La suma de los dígitos del número ingresado es: {}".format(m))