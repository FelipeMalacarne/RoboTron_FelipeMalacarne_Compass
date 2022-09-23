'''
Construa um programa que armazena uma idade em uma váriavel e compara, se a idade for maior que 18, apresenta "Maior de idade", se a idade for menor que 12, apresenta "Você é uma criança" e se for maior que 12 e menor que 18, apresenta "Você é um adolescente"
'''

def MaiorIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    elif idade <= 12:
        return "Você é uma criança"
    elif idade > 12 and idade < 18:
        return "Você é um adolescente" 

def main():
    idade = int(input("Qual é a sua idade? "))
    print(MaiorIdade(idade))

main()