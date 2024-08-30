import random

def noppa():
    r = random.randint(1,6)
    print (r)
    return r

while True:
    if noppa() == 6:
        break

