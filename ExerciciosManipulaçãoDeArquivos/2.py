import json

#abre o .json e o armazena em um python dict
with open('partida.json', 'r', encoding='utf-8') as json_origem:
    partida_dict = json.load(json_origem)


pontos_mandante =  partida_dict['copa-do-brasil'][0]['placar_mandante']
pontos_visitante = partida_dict['copa-do-brasil'][0]['placar_visitante']

if pontos_mandante > pontos_visitante :
    vencedor = 'time_mandante'
else:
    vencedor = 'time_vistante'


print (f"O time vencedor eh : {partida_dict['copa-do-brasil'][0][vencedor]['nome_popular']}")
    