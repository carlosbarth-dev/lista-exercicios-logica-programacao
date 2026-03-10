# Exercício 1 - Monitor Simples de Memória RAM

# importo as bibliotecas que preciso
import psutil  # psutil lê informações do sistema de forma fácil
import time    # time.sleep() para pausar o programa por x segundos

# loop infinito para atualizar as informações continuamente
while True:
    # psutil.virtual_memory() retorna todas as info sobre RAM
    # a função retorna um objeto com vários atributos úteis
    memoria = psutil.virtual_memory()

    # extraio as informações do objeto memoria
    # total: a quantidade total de RAM em bytes
    # used: quanto está sendo usada
    # available: quanto está disponível
    # percent: porcentagem de uso
    total = memoria.total / (1024 ** 3)      # converto para GB (divide por 1024^3)
    usada = memoria.used / (1024 ** 3)       # converto para GB
    livre = memoria.available / (1024 ** 3)  # converto para GB
    percentual = memoria.percent             # já vem em %

    # limpo a tela para melhor visualização (funciona no Windows)
    # obs: em Linux/macOS usar os.system("clear") em vez de "cls"
    import os
    os.system("cls")

    # exibo as informações de forma organizada
    print("\n" + "="*50)
    print("       MONITOR DE MEMÓRIA RAM")
    print("="*50)
    print(f"Total de RAM:     {total:.2f} GB")
    print(f"RAM em uso:       {usada:.2f} GB")
    print(f"RAM disponível:   {livre:.2f} GB")
    print(f"Utilização:       {percentual}%")
    print("="*50)
    print("Atualizando a cada 2 segundos...")
    print("Pressione Ctrl+C para interromper")

    # pausar por 2 segundos antes de atualizar novamente
    time.sleep(2)

# Anotações:
# - psutil.virtual_memory() retorna um objeto namedtuple com:
#   * total: RAM total em bytes
#   * used: RAM utilizada em bytes
#   * available: RAM disponível em bytes
#   * percent: porcentagem de uso
#   * free: RAM livre em bytes
# - para converter bytes para GB, divido por (1024^3)
#   * 1 KB = 1024 bytes
#   * 1 MB = 1024 KB
#   * 1 GB = 1024 MB
#   * total: 1 GB = 1024 * 1024 * 1024 = 1024^3 bytes
# - os.system("cls") limpa o terminal no Windows
# - time.sleep(2) pausa a execução por 2 segundos
# -:.2f formata o número com 2 casas decimais
# - while True cria um loop infinito; Ctrl+C interrompe
