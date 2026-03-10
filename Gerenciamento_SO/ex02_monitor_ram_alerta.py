# Exercício 2 - Monitor de RAM com Alerta

# importo as bibliotecas necessárias
import psutil
import time
import os

# leio do usuário o limite de RAM que vai disparar o alerta
print("="*50)
print("       MONITOR DE RAM COM ALERTA")
print("="*50)
limite_alerta = float(input("Digite o limite de uso de RAM para alerta (%): "))
print("="*50)
print("Monitorando... Pressione Ctrl+C para interromper\n")

# guardo o tempo para saber quando foi o último alerta
# assim não exibe alerta a cada atualização, mas apenas quando muda
ultimo_alerta = False

# loop infinito para monitorar continuamente
while True:
    try:
        # obtenho as informações de memória
        memoria = psutil.virtual_memory()

        # extraio as informações que preciso
        total = memoria.total / (1024 ** 3)      # converto para GB
        usada = memoria.used / (1024 ** 3)       # converto para GB
        livre = memoria.available / (1024 ** 3)  # converto para GB
        percentual = memoria.percent             # % de uso

        # limpo a tela
        os.system("cls")

        # exibo o status atual
        print("\n" + "="*50)
        print("       MONITOR DE RAM COM ALERTA")
        print("="*50)
        print(f"Total de RAM:     {total:.2f} GB")
        print(f"RAM em uso:       {usada:.2f} GB")
        print(f"RAM disponível:   {livre:.2f} GB")
        print(f"Utilização:       {percentual}%")
        print(f"Limite de alerta: {limite_alerta}%")
        print("="*50)

        # verifico se o uso ultrapassou o limite
        if percentual >= limite_alerta:
            # se ultrapassou, exibo um alerta em destaque
            print("\n⚠️  ALERTA! Uso de RAM acima do limite!")
            print(f"    Uso: {percentual}% | Limite: {limite_alerta}%")
            ultimo_alerta = True
        else:
            # se estava em alerta mas agora normalizou, informo
            if ultimo_alerta:
                print("\n✓ RAM retornou ao normal")
            ultimo_alerta = False

        print("\nAtualizando a cada 2 segundos...")
        print("Pressione Ctrl+C para interromper")

        # pauso 2 segundos
        time.sleep(2)

    except KeyboardInterrupt:
        # se o usuário pressionar Ctrl+C, o programa encerra gracefully
        print("\n\nPrograma interrompido pelo usuário.")
        break

# Anotações:
# - float() converte a entrada do usuário em número decimal
# - percentual >= limite_alerta verifica se ultrapassou
# - if/else controla se deve exibir alerta ou não
# - ultimo_alerta é uma variável de flag; flag é um marcador (True/False)
#   que ajuda a controlar se uma ação ja foi feita ou não
# - try/except com KeyboardInterrupt trata quando usuário pressiona Ctrl+C
#   Ctrl+C lança uma exceção KeyboardInterrupt, que posso capturar
# - break sai do loop while
# - ⚠️ e ✓ são emoji unicode para deixar mais visual
