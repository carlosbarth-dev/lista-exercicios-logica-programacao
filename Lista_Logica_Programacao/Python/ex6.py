# Exercício 6 - Contar vogais

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)

# Anotações:
# - Criei uma string com todas as vogais
# - Percorri cada letra da frase com for
# - Usei "in" para verificar se a letra está dentro da string de vogais
# - contador += 1 incrementa 1 a cada vogal encontrada
# - Python facilita muito manipulação de texto