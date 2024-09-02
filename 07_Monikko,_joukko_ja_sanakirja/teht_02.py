nimet = set()

while True:
    ni = input("Anna nimi:")
    if ni == "":
        break
    elif ni in nimet:
        print("Aiemmin syötetty nimi")
    elif ni not in nimet:
        print("Uusi nimi")
    nimet.add(ni)
for i in nimet:
    print(i)