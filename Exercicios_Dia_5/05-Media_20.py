'''
Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados
'''
def is_even(n):
    return n % 2 == 0

def main():
    soma = 0
    counter = 0

    for i in range(0,20):
        num = int(input(f"Informe o número de indice {i}: "))
        if is_even(num):
            soma += num
            counter += 1
    media = soma/counter

    print(f"A média aritmética da lista de números é: {media}")

main()