def summa(x):
    r = sum(x)
    return r
lista = []

while True:
    t = int(input("Anna luku: "))
    if t < 0:
        break
    lista.append(t)
print(summa(lista))