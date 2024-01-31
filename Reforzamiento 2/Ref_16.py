milista = []

entero = 0

while entero <= 100:
    milista.append(entero)
    entero += 1

rango = range(10,35)
i = min(rango)
while i <= max(rango):
    print(milista[i])
    i +=1