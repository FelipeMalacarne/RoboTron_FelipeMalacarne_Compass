#inicializa lista
numList = []

#Função pega apenas números pares e monta a lista
def getNumList(size):
    for i in range(0, size):
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
    counter = 0
    for i in range(0, len(list)):
        soma += list[i]
        counter += 1

    return soma/counter

getNumList(20)
media = calcularMedia(numList)

print(f"A média aritmética da lista de números é: {media}")
