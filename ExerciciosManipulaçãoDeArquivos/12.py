'''
Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")

#Seleciona as linhas cujo os respectivos anos batem e a coluna "Name"
vencedores = arquivo.loc[(arquivo["Year"] == 1991) | (arquivo["Year"] == 2016), "Name"]

#Armazena apenas os valores em uma lista
vencedores = vencedores.values

#Mostra os nomes
for i in vencedores:
    print(i)
