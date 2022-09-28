import json

with open('partida.json', 'r', encoding='utf-8') as json_origem:
    partida_dict = json.load(json_origem)
    nome_estadio = partida_dict['copa-do-brasil'][0]['estadio']['nome_popular']
    placar = partida_dict['copa-do-brasil'][0]['placar']
    status = partida_dict['copa-do-brasil'][0]['status']

    print(f'O nome do estadio eh: {nome_estadio}')
    print(f'O placar da partida eh: {placar}') 
    print(f'O status da partida eh: {status}')