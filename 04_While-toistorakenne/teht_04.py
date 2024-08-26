import random

numero = random.randint(1, 10)

while True:
    print (numero)
    arv = int(input("Numero: "))
    if arv == numero:
        print("Oikein")
        break
    elif arv > numero:
        print("Liian suuri arvaus")
    elif arv < numero:
        print("Liian pieni arvaus")
