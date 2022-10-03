'''
Guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.
'''

import json

#abre o .json e o armazena em um python dict
with open('campeonato.json', 'r', encoding='utf-8') as json_origem:
    campeonato_dict = json.load(json_origem)
    
#converte o python dict em uma string identada
string_json_formatado = json.dumps(campeonato_dict, indent=2)
print(string_json_formatado)