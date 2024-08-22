leiviska = input("Anna leiviskät: ")
naula = input("Anna naulat: ")
luoti = input("Anna luodit: ")

naula = float(naula) + 20*float(leiviska)
luoti = float(luoti) + 32*naula

g = 13.3*luoti

kilot = int(g // 1000)
grammat = g % 1000

print (f"Massa nykymittojen mukaan: {kilot} kilogrammaa ja {grammat:.2f} grammaa.")
