import os

def mostrar_propriedade(tabela):
    while True:
        print("Propriedades: Simbolo / Nome / NumeroAtomico / Linha / Coluna / EstadoFisico\n")

        propriedade = input("Selecione uma propriedade para mostrar: ")

        propriedades_disponíveis = ["Simbolo", "Nome", "NumeroAtomico", "Linha", "Coluna", "EstadoFisico"]

        if propriedade in propriedades_disponíveis:
            
            print(tabela[propriedade])
        else:
            print("Informe uma escolha válida !\n")
            input("Pressione Enter para continuar...\n")
            os.system('cls')
            continue

        input("Pressione Enter para voltar à tela inicial...")
        os.system('cls')
        break