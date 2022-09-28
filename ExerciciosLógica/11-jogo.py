'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
'''

def main():
    horaInicial = int(input("Informe a hora inicial "))
    horaFinal = int(input("Informe a hora final "))

    if horaFinal > horaInicial:
        duracao = horaFinal - horaInicial
    else:
        duracao = (horaFinal + 24) - horaInicial

    print(f"O JOGO DUROU {duracao} HORA(S)")
main()