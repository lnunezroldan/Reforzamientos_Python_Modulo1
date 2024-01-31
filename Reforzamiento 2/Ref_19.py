lista = []
valor1 = lista.append(input("Introduzca su numero 1: "))
valor2 = lista.append(input("Introduzca su numero 2: "))
valor3 = lista.append(input("Introduzca su numero 3: "))
valor4 = lista.append(input("Introduzca su numero 4: "))
valor5 = lista.append(input("Introduzca su numero 5: "))
valor6 = lista.append(input("Introduzca su numero 6: "))
valor7 = lista.append(input("Introduzca su numero 7: "))
valor8 = lista.append(input("Introduzca su numero 8: "))
valor9 = lista.append(input("Introduzca su numero 9: "))
valor10 = lista.append(input("Introduzca su numero 10: "))

tamaño = len(lista)

suma = 0
for i in lista:
    suma += int(i)

print("La lista está conformada por: {}".format(lista))
print("La suma de los valores de la lista es: {}".format(suma))
print("La media de los valores de la lista es: {}".format(suma/tamaño))
