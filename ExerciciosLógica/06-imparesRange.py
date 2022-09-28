'''
Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x
'''


def isEven(n):
    return n % 2 == 0

def main():
    maxRange = int(input("Informe um valor inteiro maior que 2: "))

    print(f"O os números ímpares entre 2 e {maxRange} são: ")

    #Itera por todos números até maxRange, mostra os não-pares
    for i in range(2, maxRange):
        if not isEven(i):
            print(i)

main()