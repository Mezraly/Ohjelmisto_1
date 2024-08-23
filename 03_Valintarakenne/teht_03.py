suku = input("Sukupuoli: ")
hemo = int(input("Hemoglobiini(g/l): "))

if suku == "mies" or suku == "Mies":
    if hemo < 134:
        print("Hemoglobiini arvo on alhainen")
    elif hemo > 195:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Hemoglobiini arvo normaali")
elif suku == "nainen" or suku == "Nainen":
    if hemo < 117:
        print("Hemoglobiini arvo on alhainen")
    elif hemo > 175:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Hemoglobiini arvo normaali")