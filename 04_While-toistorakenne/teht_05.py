user = "python"
passw = "rules"

yri = 5

while yri > 0:
    k1 = input("Käyttäjä: ")
    k2 = input("Salasana")
    if k1 == user and k2 == passw:
        print("Tervetuloa")
        break
    yri -= 1
if yri == 0:
    print("Pääsy evätty")