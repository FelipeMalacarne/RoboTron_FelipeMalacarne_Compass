def MaiorIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    elif idade <= 12:
        return "Você é uma criança"
    elif idade > 12 and idade < 18:
        return "Você é um adolescente" 

idade = int(input("Qual é a sua idade? "))
print(MaiorIdade(idade))
