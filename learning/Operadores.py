"""
Operadores aritméticos
    Adição: +
    Subtração: -
    Divisão: /
    Divisão Inteira: //
    Resto: %
    Potência **

Operadores de Comparação (autoexplicativo)
    >
    <
    ==
    !=
    >=
    <=

Operadores Lógicos (autoexplicativo)
    and
    or
    not

Operadores de indentidade
    is  #retorna true se as variaveis comparadas forem o mesmo objeto Ex: name is marcos
    is not #O mesmo porém retorna o oposto

Operadores de indentidade
    in #retorna True caso o valor seja encontrado na sequencia ex: 2 in x
    not in #O mesmo porém retorna o oposto
"""

x = {
    "nome": "Felipe",
    "sobrenome": "Malacarne"
}
y = x
print(y is x)

z = {
    "nome": "Felipe",
    "sobrenome": "Malacarne"
}
print(z is x)

