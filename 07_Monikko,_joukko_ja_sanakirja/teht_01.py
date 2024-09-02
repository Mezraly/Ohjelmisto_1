aika = ("Talvi", "Kevät", "Kesä", "Syksy")
num = int(input("Anna kuukausi (1-12): "))

if num in range(3, 6):
    print(aika[1])
elif num in range(6, 9):
    print(aika[2])
elif num in range(9, 12):
    print(aika[3])
elif num in range(1, 3) or num == 12:
    print(aika[0])