'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
'''

def main():
    hora_inicial = int(input("Informe a hora inicial "))
    hora_final = int(input("Informe a hora final "))

    if hora_final > hora_inicial:
        duracao = hora_final - hora_inicial
    else:
        duracao = (hora_final + 24) - hora_inicial

    print(f"O JOGO DUROU {duracao} HORA(S)")
main()