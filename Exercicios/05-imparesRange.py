def isEven(n):
    return n % 2 == 0

maxRange = int(input("Informe um valor inteiro maior que 2: "))

print(f"O os números ímpares entre 2 e {maxRange} são: ")
for i in range(2, maxRange):
    if not isEven(i):
        print(i)
