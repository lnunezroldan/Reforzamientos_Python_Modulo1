oracion = input("Ingrese una frase con un minimo de 3 palabras:")
def wordcount(a):
    x = str(a)
    return len(x.split())

m = wordcount(oracion)
print("El numero de palabras es: {}".format(m))
