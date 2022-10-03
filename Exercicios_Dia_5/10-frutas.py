'''
Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"]
##Checar se as duas listas são exatamente iguais.
'''
def main():
    lista_fixa = ["maça", "banana", "pera"]
    match_counter = 0
    for i in range(0,3):
        aux = input(f"Informe a {i+1} fruta : ")
        if aux == lista_fixa[i]:
            match_counter += 1
   
    if match_counter == 3:
        print("As duas listas são iguais ")
    else:
        print("As listas não são iguais ")
main()