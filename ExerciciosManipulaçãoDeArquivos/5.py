import json

#abre o .json e o armazena em um python dict
with open('campeonato.json', 'r', encoding='utf-8') as json_origem:
    campeonato_dict = json.load(json_origem)
    
#converte o python dict em uma string identada
stringJson_formatado = json.dumps(campeonato_dict, indent=2)
print(stringJson_formatado)