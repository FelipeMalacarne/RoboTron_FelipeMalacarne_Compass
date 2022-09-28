texto = "String exemplo para teste"

#percorrer um range de caracteres
print(texto[0:6])

#numero final pode ser omitido
print(texto[7:])

#Achar carcteres, retorna posição do primeiro encontrado
print(texto.find("e"))

#corta a string no caractere informado, retorna lista
print(texto.split(" "))