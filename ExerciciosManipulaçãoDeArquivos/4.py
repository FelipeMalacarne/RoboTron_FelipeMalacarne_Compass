'''
Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.
'''

import json

with open('partida.json', 'r', encoding='utf-8') as json_origem:
    partida_dict = json.load(json_origem)

time_visitante = partida_dict['copa-do-brasil'][0]['time_visitante']

visitante_formatado = json.dumps(time_visitante, indent=2, ensure_ascii=False)

print(visitante_formatado)