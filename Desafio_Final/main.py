import os
import pandas as pd

from Mostrar_Propriedade import mostrar_propriedade
from Mostrar_Elemento import mostrar_elemento
from Mostrar_Tudo import mostrar_tudo

#utiliza o pandas para ler o csv, define tabela global
tabela = pd.read_csv("Tabela_Periódica.csv", encoding="UTF-8", sep=",")

#Função principal
def main():
    os.system('cls')
    while True:
        print("Para fechar o programa use Ctrl-C\n\n")
        print("Escolha uma função: ")
        print("1 - Mostrar apenas propriedade selecionada, de todos elementos")
        print("2 - Mostrar todas Propriedades de um dado elemento")
        print("3 - Mostrar todos dados dos elementos ")

        escolha = input("\n")
        os.system('cls')

        if escolha == "1":
            mostrar_propriedade(tabela)      
        elif escolha == "2":
            mostrar_elemento(tabela)
        elif escolha == "3":
            mostrar_tudo(tabela) 
        else:
            print("Informe uma escolha válida! ")
            input("Pressione Enter para continuar...")
            os.system('cls')
main()