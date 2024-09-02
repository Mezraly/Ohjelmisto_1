def odd(x):
    for i in x:
        if i % 2 == 1:
            x.remove(i)
    return x
lista = []

while True:
    t = int(input("Anna luku: "))
    if t < 0:
        break
    lista.append(t)
print(lista)
print(odd(lista))