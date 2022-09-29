'''
Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.
'''
import json

#abre o .json e o armazena em um python dict
with open('campeonato.json', 'r', encoding='utf-8') as json_origem:
    campeonato_dict = json.load(json_origem)
    
edicao_atual = campeonato_dict["edicao_atual"]
fase_atual = campeonato_dict["fase_atual"]
rodada_atual = campeonato_dict["rodada_atual"]

lista = [edicao_atual, fase_atual, rodada_atual]

for i in lista:
    for j in i:
        print(f"\"{j}\": \"{i[j]}\"")
        break






'''
for i in edicao_atual:
    print(f"\"{i}\": \"{edicao_atual[i]}\"")
    break

for i in fase_atual:
    print(f"\"{i}\": \"{fase_atual[i]}\"")
    break

for i in rodada_atual:
    print(f"\"{i}\": \"{rodada_atual[i]}\"")
    break
'''