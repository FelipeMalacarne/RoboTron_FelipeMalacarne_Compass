import os

#Retorna uma lista com toda coluna "0", todos simbolos
def pegar_todos_simbolos(tabela):
    return tabela.iloc[:, 0].tolist()

def mostrar_elemento(tabela):
    while True:
        elemento = input("Insira o simbolo do elemento que deseja vizualizar: ")

        elementos_disponíveis = pegar_todos_simbolos(tabela)

        if elemento in elementos_disponíveis:
            #Pega a linha que bate com o simbolo do input
            print(f"\n{tabela.loc[tabela['Simbolo'] == elemento]}\n")
        else:
            print("")
            print("\nEsse Elemento não está presente no CSV, escolha outro!\n")
            print(f"Elementos dispponíveis: {elementos_disponíveis}\n")
            input("Pressione Enter para continuar...")
            os.system('cls')
            continue
        
        input("Pressione Enter para voltar à tela inicial...")
        os.system('cls')
        break

