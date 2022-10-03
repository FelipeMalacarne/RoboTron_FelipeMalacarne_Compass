'''
Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o como partida guarde em uma variável e printe o JSON inteiro no terminal.
'''


import json

#abre o .json e o armazena em um python dict
with open('partida.json', 'r', encoding='utf-8') as json_origem:
    partida_dict = json.load(json_origem)
    
#converte o python dict em uma string identada
string_json_formatado = json.dumps(partida_dict, indent=2)
print(string_json_formatado)