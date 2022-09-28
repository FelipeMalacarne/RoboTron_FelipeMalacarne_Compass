import pandas as pd

arquivo = pd.read_csv('TesteLeituraCSV.csv', encoding='UTF-8', sep=',')
# print(arquivo)


arquivoCol = pd.read_csv('TesteLeituraCSV.csv', encoding='UTF-8', sep=',', usecols=["Nome", "Sobrenome"])
# print(arquivoCol)

# print(arquivo[["Area", "Nome"]].head())

# print(arquivo.Email.head())
print(arquivo.loc[1:2])