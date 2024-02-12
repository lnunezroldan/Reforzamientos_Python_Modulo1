usuario = input("Ingrese los valores que desea incluir en la lista separados por una coma: ")
usuario1 = input("Ingrese el valor que desea eliminar de la lista inicial: ")

lista = usuario.split(", ")
def borra(a, b):
    l = a.split(", ")
    l.remove(b)
    return l

m = borra(usuario,usuario1)
print("La lista inicial es: {}".format(lista))
print("La lista actualizada es: {}".format(m))