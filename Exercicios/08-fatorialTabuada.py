'''
Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x em uma função e apresentar o resultado fora da função. Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X.
'''
#Retorna True caso par
def isEven(n):
    return n % 2 == 0

#Calcula fatorial de 'n' recursivamente
def fatorial(n):
    if n < 2:
        return n
    return fatorial(n-1) * n   

#Mostra a tabuada de 'n'
def mostrarTabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def main():
    x = int(input("Informe um valor inteiro para X: "))
    
    if isEven(x):
        print(f"Fatorial de {x} eh {fatorial(x)}")
    else:
        mostrarTabuada(x)
main()