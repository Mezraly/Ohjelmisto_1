kirja = {"EFAH":"Ahmosuo Airport",
         "EFAL":"Alavus Airport",
         "EFET":"Enontekiö Airport",
         "EFFO":"Forssa Airport",
         "EFHA":"Halli Airport",
         "EFHF":"Helsinki-Malmi Airport",
         "EFHK":"Helsinki-Vantaa Airport",
         "EFIV":"Ivalo Airport",
         "EFLP":"Lappeenranta Airport",
         "EFRO":"Rovaniemi Airport"
         }
while True:
    inp = input("Lisää(L), Hae(H), Lopeta(Q): ")
    if inp == "Q":
        break
    elif inp == "H":
        haku = input("Hae: ")
        if haku in kirja:
            print(kirja[haku])
        else:
            print("Ei löytynyt")
    elif inp == "L":
        ic = input("Anna ICAO: ")
        nimi = input("Anna nimi: ")
        if ic == "" or nimi == "":
            print("Ei tyhjää")
        elif ic != "" and nimi != "":
            kirja[ic] = nimi
    else:
        print("Yritä uudestaan")