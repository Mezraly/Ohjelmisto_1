num = int(input("Numero: "))

if num > 1:
    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            print(num, "Ei ole alkuluku")
            break
    else:
        print(num, "On alkuluku")
else:
    print(num, "Ei ole alkuluku")