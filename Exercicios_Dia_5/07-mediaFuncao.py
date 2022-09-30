'''
Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores
'''

def Media(num1, num2):
    return (num1 + num2)/2 

def main():
    num1 = int(input("Informe o primeiro valor inteiro: "))
    num2 = int(input("Informe o segundo valor inteiro: "))
    media = Media(num1, num2)
    print (f"A média dos dois inteiros eh: {media}")

main()