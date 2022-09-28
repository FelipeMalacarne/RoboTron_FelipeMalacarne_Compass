import json

#abre o .json e o armazena em um python dict
with open('campeonato.json', 'r', encoding='utf-8') as json_origem:
    campeonato_dict = json.load(json_origem)
    
edicao_atual = campeonato_dict["edicao_atual"]
fase_atual = campeonato_dict["fase_atual"]
rodada_atual = campeonato_dict["rodada_atual"]

edicao_first = list(edicao_atual.items())[0]
fase_first = list(fase_atual.items())[0]
rodada_first = list(rodada_atual.items())[0]

print("edicao_atual")
print(f"{edicao_first[0]} : {edicao_first[1]}")
print(json.dumps(edicao_first, indent=2))

print("fase_atual")
print(json.dumps(fase_atual, indent=2))

print("rodada_atual")
print(json.dumps(rodada_atual, indent=2))