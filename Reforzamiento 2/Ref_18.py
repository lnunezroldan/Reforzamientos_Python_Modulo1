impares = []

i = 1

while i < 30:
    impares.append(i)
    i +=2

impares.append(27.0)
impares.append(27.0)
impares.append(27.0)
impares.insert(3, "Nulo")

print(impares)

del impares[3]
print("La lista final sería: {}".format(impares))