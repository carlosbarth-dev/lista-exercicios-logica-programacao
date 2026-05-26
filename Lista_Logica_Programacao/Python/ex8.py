# Exercício 8 - Jogo de Adivinhação

import random  # usamos a biblioteca random para sortear números

# sorteio do número entre 1 e 100 (inclusive)
numero = random.randint(1, 100)

# contador de tentativas começa em zero
tentativas = 0

# loop while para repetir até o usuário acertar
while True:
    # pede palpite e converte para int porque input é texto
    palpite = int(input("Digite um palpite (1-100): "))
    tentativas += 1  # cada interação conta uma tentativa

    # verifica se acertou ou dá dica
    if palpite == numero:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break  # sai do loop quando acerta
    elif palpite < numero:
        print("Tente um número maior.")  # dica: chute maior
    else:
        print("Tente um número menor.")  # dica: chute menor

# Anotações:
# - usei random.randint(1, 100) porque ele devolve um inteiro aleatório entre os limites.
# - while True cria um laço infinito que só termina com break quando o palpite está correto.
# - contador de tentativas é importante para saber quantas jogadas o usuário fez.
# - if/elif/else servem para comparar o palpite com o número e dar dica de "maior" ou "menor".
# - converti o input para int porque input sempre retorna string, e precisamos comparar números.
# - coloquei comentários explicando cada parte, igual às outras atividades, para revisar depois e explicar ao professor.