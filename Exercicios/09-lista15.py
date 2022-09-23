'''
Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do ultimo para o primeiro
'''

def main():
    list = []
    #preenche a lista 15 valores
    for i in range(0,15):
        x = input(f"Informe um valor para indice {i} da lista: ")
        list.append(x)

    #Mostra os valores do ultimo ao primeiro
    for i in reversed(range(0, 15)):
        print(list[i])

main()