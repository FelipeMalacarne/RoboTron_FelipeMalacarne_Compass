'''
Crie mais uma coluna em tempo de execução juntando os dados movie e year
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")


#Cria nova coluna "Filme_ano", como a coluna Year é inteiro, necessário converter para str
arquivo["Filme_Ano"] = arquivo['Movie'] + ", " + arquivo['Year'].astype(str)

print(arquivo["Filme_Ano"])