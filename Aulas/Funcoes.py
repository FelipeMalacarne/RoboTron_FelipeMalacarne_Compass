
#Soma simples
def somar(num1, num2):
    soma = num1 + num2
    return soma

# print(f"A soma de 5 e 2 eh: {somar(5, 2)}")

#Recursiva Fibonacci
def getNFibo(n):
    if n < 2:
        return n
    return getNFibo(n-1) + getNFibo(n-2)

# print(f'O elemento 10 da sequencia de fibonacci eh: {getNFibo(10)}')

def acharFelipe(list):
    if "Felipe" in list:
        print("Felipe esta na lista")
    else:
        assert False, "Felipe não esta na lista "

# listaTeste = ["Ramiro", "Lucas", "Felipe", "Luiz"]
# listaTeste2 = ["Ramiro", "Lucas", "Romulo", "Luiz"]
# acharFelipe(listaTeste)
# acharFelipe(listaTeste2)





