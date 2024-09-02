from math import pi
def pizza(r, y):
    m2 = pi * (r/2) ** 2
    c = y/m2
    return c

p1 = int(input("Pizza 1 halkaisija: "))
h1 = int(input("Pizza 1 hinta: "))
p2 = int(input("Pizza 2 halkaisija: "))
h2 = int(input("Pizza 2 hinta: "))

if pizza(p1, h1) < pizza(p2, h2):
    print("Pizza 1 halvempi")
elif pizza(p1, h1) > pizza(p2, h2):
    print("Pizza 2 halvempi")
else:
    print("Sama pizza")