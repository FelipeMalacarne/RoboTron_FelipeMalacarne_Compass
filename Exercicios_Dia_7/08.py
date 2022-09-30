'''
Abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal
'''

import pandas as pd

arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")

#Aumenta o max_rows para mostrar todos os valores no console
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

print(arquivo)