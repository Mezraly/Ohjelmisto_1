import random

num = int(input("Kuinka monta noppaa: "))
a = [random.randint(1, 6) for i in range(num)]
print(a)