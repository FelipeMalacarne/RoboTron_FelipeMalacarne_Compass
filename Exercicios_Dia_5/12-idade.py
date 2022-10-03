'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias. Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
'''
#Converte uma idade em dias, meses e anos
def converter_idade(idade):
    anos = idade // 365
    idade %= 365
    meses = idade // 30
    idade %= 30
    dias = idade

    return {
        "anos": anos,
        "meses": meses,
        "dias": dias
    }
  
def main():
    idade = int(input("Informe uma idade em dias: "))
    idade = converter_idade(idade)

    print(f"{idade['anos']} ano(s)")
    print(f"{idade['meses']} mes(es)")
    print(f"{idade['dias']} dia(s)")

main()