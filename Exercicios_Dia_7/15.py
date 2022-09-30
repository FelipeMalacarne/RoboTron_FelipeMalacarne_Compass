'''
Mostre todos os filmes menos o “The Revenant”.
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")

filmes = arquivo.loc[arquivo["Movie"] != "The Revenant" , "Movie"]

#Aumenta o max_rows para mostrar todos os valores no console
pd.set_option('display.max_rows', 200)

print(filmes)