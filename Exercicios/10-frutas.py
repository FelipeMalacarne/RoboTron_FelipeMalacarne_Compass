'''
Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"]
##Checar se as duas listas são exatamente iguais.
'''
def main():
    listaFixa = ["maça", "banana", "pera"]
    matchCounter = 0
    for i in range(0,3):
        aux = input(f"Informe a {i+1} fruta : ")
        if aux == listaFixa[i]:
            matchCounter += 1
   
    if matchCounter == 3:
        print("As duas listas são iguais ")
    else:
        print("As listas não são iguais ")
main()