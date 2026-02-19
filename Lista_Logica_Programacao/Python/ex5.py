# Exercício 5 - Par ou Ímpar

numero = int(input("Digite um número: "))

# % retorna resto da divisão
if numero % 2 == 0:
    print("É par")
else:
    print("É ímpar")

# Anotações:
# - Usei % para pegar o resto da divisão
# - Se o resto for 0 significa que é divisível por 2
# - if em Python não usa parênteses obrigatórios
# - Precisa de dois pontos ":" depois do if