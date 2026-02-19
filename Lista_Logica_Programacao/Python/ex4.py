# Exercício 4 - Tabuada

numero = int(input("Digite um número: "))

# usei for para repetir de 1 até 10
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

# Anotações:
# - Usei for porque preciso repetir 10 vezes
# - range(1, 11) vai do 1 até o 10 (o 11 não entra)
# - numero * i faz a multiplicação da tabuada
# - Python é simples porque o for já funciona direto com range