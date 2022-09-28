import json

#abre o .json e o armazena em um python dict
with open('partida.json', 'r', encoding='utf-8') as json_origem:
    partida_dict = json.load(json_origem)
    
#converte o python dict em uma string identada
stringJson_formatado = json.dumps(partida_dict, indent=2)
print(stringJson_formatado)