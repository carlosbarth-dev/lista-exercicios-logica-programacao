# Exercício 7 - Lista de números

quantidade = int(input("Quantos números você quer digitar? "))

numeros = []

for i in range(quantidade):
    num = float(input("Digite um número: "))
    numeros.append(num)  # adiciona na lista

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print("Maior:", maior)
print("Menor:", menor)
print("Média:", media)

# Anotações:
# - Usei lista porque a quantidade é variável
# - append() adiciona elemento na lista
# - max() e min() já existem prontos em Python
# - sum() soma todos os elementos
# - len() retorna o tamanho da lista
# - Python tem muitas funções prontas que facilitam