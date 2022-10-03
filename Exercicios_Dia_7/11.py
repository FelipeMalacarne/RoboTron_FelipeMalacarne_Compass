'''
Printe o nome do Ator que ganhou o Oscar em 1993.
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")

# .loc[linha, coluna]
oscar_93 = arquivo.loc[arquivo["Year"] == 1993, "Name"]

# '.values' transforma o df e retorna uma lista com a apenas os valores, no caso é uma lista com apenas 1 item
print(oscar_93.values[0])