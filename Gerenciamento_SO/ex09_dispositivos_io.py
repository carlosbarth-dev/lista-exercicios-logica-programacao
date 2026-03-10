# Exercício 9 - Listagem de Dispositivos de Entrada e Saída

# importo as bibliotecas
import psutil
import os

# limpo a tela
os.system("cls")

print("="*80)
print("       GERENCIADOR DE DISPOSITIVOS DE ENTRADA E SAÍDA (E/S)")
print("="*80)

# ============================================================
# CONCEITO: O que são dispositivos de E/S?
# ============================================================

print("\n[CONCEITO] Dispositivos de Entrada e Saída:")
print("-" * 80)

print("""
Dispositivos de E/S são periféricos que permitem o computador se comunicar
com o mundo externo.

Exemplos práticos:

- ARMAZENAMENTO (E/S):
    * HDs (Hard Drives)
    * SSDs (Solid State Drives)
    * Pendrives
    * DVDs/CDs
    * Fitas magnéticas

- ENTRADA (INPUT):
    * Teclado
    * Mouse
    * Joystick
    * Câmera
    * Microfone
    * Scanner

- SAÍDA (OUTPUT):
    * Monitor/Tela
    * Impressora
    * Alto-falante
    * Projetor

- REDE (Entrada E Saída):
    * Placa de rede
    * Modem

Neste exercício, focamos em dispositivos de ARMAZENAMENTO
detectados via psutil.
""")

print("="*80)

# ============================================================
# PARTE PRÁTICA
# ============================================================

print("\n[PRÁTICA] Dispositivos de Armazenamento Detectados:")
print("-" * 80)

particoes = psutil.disk_partitions()

if not particoes:
    print("Nenhuma partição encontrada!")
else:
    print(f"{'#':<3} {'Dispositivo':<15} {'Ponto Montagem':<20} {'Tipo':<10}")
    print("-" * 80)

    for idx, particao in enumerate(particoes, 1):
        device = particao.device
        mountpoint = particao.mountpoint
        fstype = particao.fstype if particao.fstype else "N/A"

        print(f"{idx:<3} {device:<15} {mountpoint:<20} {fstype:<10}")

# ============================================================
# MENU PARA DETALHES
# ============================================================

if particoes:
    print("\n" + "="*80)
    print("[MENU] Selecionar um dispositivo para detalhes:")
    print("-" * 80)

    try:
        escolha = int(input(f"Digite o número do dispositivo (1-{len(particoes)}): "))

        if 1 <= escolha <= len(particoes):
            particao_escolhida = particoes[escolha - 1]
            mountpoint = particao_escolhida.mountpoint

            try:
                info = psutil.disk_usage(mountpoint)

                total_gb = info.total / (1024 ** 3)
                usado_gb = info.used / (1024 ** 3)
                livre_gb = info.free / (1024 ** 3)
                percentual = info.percent

                print("\n" + "="*80)
                print(f"Detalhes do Dispositivo: {particao_escolhida.device}")
                print("="*80)
                print(f"Ponto de Montagem:      {mountpoint}")
                print(f"Tipo de Sistema Arquivo:{particao_escolhida.fstype}")
                print(f"\nEspaço Total:           {total_gb:.2f} GB")
                print(f"Espaço Usado:           {usado_gb:.2f} GB ({percentual:.1f}%)")
                print(f"Espaço Livre:           {livre_gb:.2f} GB ({100-percentual:.1f}%)")
                print("="*80)

            except PermissionError:
                print("Erro: Sem permissão para acessar este dispositivo.")
        else:
            print("Número inválido!")

    except ValueError:
        print("Entrada inválida! Digite um número.")

print("\n")

# Anotações:
# - Dispositivos de E/S transferem dados
# - ARMAZENAMENTO é detectável via psutil
# - INPUT envia dados para o computador
# - OUTPUT recebe dados do computador
# - Alguns dispositivos são bidirecionais (ex: rede)
# - psutil detecta apenas armazenamento
# - Outros dispositivos exigem WMI (Windows) ou /proc (Linux)