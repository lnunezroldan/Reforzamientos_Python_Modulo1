milista = [25.6, None, 28.6, False, 28.1, True]
total = len(milista)
print("Mi lista tiene {} items".format(total))

i = total - 1

while i >= 0:
    print("El item de posición {} es: {}".format(i, milista.__getitem__(i)))
    print("El tipo de dato es: {}".format(type(milista.__getitem__(i))))
    i -= 1