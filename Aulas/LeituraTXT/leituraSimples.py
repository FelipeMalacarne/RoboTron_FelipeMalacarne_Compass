with open("TesteLeitura.txt", "r", encoding="UTF-8") as arquivo:
    conteudo  = arquivo.read()
    print(conteudo)

with open("TesteLeitura.txt", "r", encoding="UTF-8") as arquivo:
    for i in reversed(arquivo.readlines()):
        print(i)
