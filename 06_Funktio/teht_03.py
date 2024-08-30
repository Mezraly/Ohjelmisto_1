def muutos(x):
    x = x*3.785
    return x

while True:
    gal = int(input("Gallonia: "))
    if gal < 0:
        break
    print(f"={muutos(gal)} Litraa")
