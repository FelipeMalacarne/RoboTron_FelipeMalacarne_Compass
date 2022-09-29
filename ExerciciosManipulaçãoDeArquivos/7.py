'''
Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.
'''

import json

#abre o .json e o armazena em um python dict
with open('campeonato.json', 'r', encoding='utf-8') as json_origem:
    campeonato_dict = json.load(json_origem)

print("principais chaves do campeonato.json")
for i in campeonato_dict:
    print(i)