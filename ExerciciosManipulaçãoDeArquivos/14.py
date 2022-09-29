'''
Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")

vencedores = arquivo.loc[(arquivo["Year"] >= 1987) & (arquivo["Year"] <= 1999), ["Name", "Age"]]

print(vencedores)