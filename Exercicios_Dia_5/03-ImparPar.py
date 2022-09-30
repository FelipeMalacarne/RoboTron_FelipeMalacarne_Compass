'''
Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar
'''

#Retorna True se for par
def isEven(n):
    return n % 2 == 0

def main():
    n = int(input("Informe um inteiro: "))
    
    if isEven(n):
        print("O numero eh Par")
    else:
        print("O numero eh Impar")
     
main()