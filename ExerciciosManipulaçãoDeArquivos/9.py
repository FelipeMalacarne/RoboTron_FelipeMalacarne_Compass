'''
Usando Pandas, leia apenas os dados da coluna Age do CSV.
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",", usecols=["Age"])
pd.set_option('display.max_rows', 200)

print(arquivo)