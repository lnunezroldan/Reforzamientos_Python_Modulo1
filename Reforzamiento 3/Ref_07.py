class Frase:
    def __init__(self, texto):
        self.texto = texto.split()

    def revertir(self):
        x = self.texto
        y = list(reversed(x))
        for palabra in y:
            print(palabra, end=" ")

frase = Frase(input("Ingresa una frase: "))
frase.revertir()





