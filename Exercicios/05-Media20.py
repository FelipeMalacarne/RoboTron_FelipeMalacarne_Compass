'''
Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados
'''

#inicializa lista
numList = []

#Função pega apenas números pares e monta a lista
def getNumList(maxRange):
    for i in range(0, maxRange):
        print(f"Informe o número de indice: {i}")
        num = int(input())
        if isEven(num):
            numList.append(num)
        else:
            continue

def isEven(n):
    return n % 2 == 0

#calcula a média dado a lista como parametro
def calcularMedia(list):
    soma = 0
    for i in range(0, len(list)):
        soma += list[i]
    return soma/len(list)

def main():
    #Requisita 20 numeros, monta a lista com os pares
    getNumList(20)
    #Calcula a média da lista com os pares
    media = calcularMedia(numList)

    print(f"A média aritmética da lista de números é: {media}")

main()