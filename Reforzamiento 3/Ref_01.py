numero1 = int(input("Ingresar un número positivo: "))
numero2 = int(input("Ingresar un número positivo: "))

"""Función de suma de dígitos"""
def sumdigits(a):
    suma = 0
    while a > 0:
        suma = suma + (a % 10)
        a = a // 10
    return suma

num1 = sumdigits(numero1)
num2 = sumdigits(numero2)

if num1 > num2:
    print("El número cuya suma de dígitos es mayor, es:{}".format(numero1))
elif num1 == num2:
    print("La suma de los dígitos de ambos números es el mismo")
else:
    print("El número cuya suma de dígitos es mayor, es:{}".format(numero2))

if num1 > 10:
    print("La suma de dígitos del número {} es mayor a 10".format(numero1))
elif num2 > 10:
    print("La suma de dígitos del número {} es mayor a 10".format(numero2))
else:
    print("La suma de dígitos de ambos números NO superan a 10")
