import random
x = int(input("tahkojen määrä: "))

def noppa(x):
    r = random.randint(1,x)
    print (r)
    return r

while True:
    if noppa(x) == x:
        break