'''
Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.
(Vou procurar o a linha especifica do filme "The Godfather")
'''

import pandas as pd

#utiliza o pandas para ler o csv
arquivo = pd.read_csv("ator.csv", encoding="utf-8", sep=",")

#retorna a linha junto com o índice do CSV contendo o filme selecionado
print(arquivo[arquivo["Movie"] == "The Godfather"])