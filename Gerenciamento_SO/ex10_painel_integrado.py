# Exercício 10 - Painel Integrado de Monitoramento (RAM + CPU + Disco + Rede)

# importo as bibliotecas necessárias
import psutil
import time
import os

# limpo a tela (funciona no Windows; em Linux/macOS trocar "cls" por "clear")
def limpar_tela():
    # detecta o sistema operacional
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux e macOS
        os.system("clear")

# variáveis para rastrear tráfego de rede
primeira_leitura_rede = True
bytes_recv_anterior = 0
bytes_sent_anterior = 0

try:
    while True:

        # ====== COLETA DE DADOS ======

        # 1. MEMÓRIA RAM
        memoria = psutil.virtual_memory()
        ram_total = memoria.total / (1024 ** 3)
        ram_usada = memoria.used / (1024 ** 3)
        ram_percentual = memoria.percent

        # 2. CPU
        # uso da CPU (espera 1 segundo para medir)
        cpu_percentual = psutil.cpu_percent(interval=1, percpu=False)

        # 3. DISCO (partição principal, normalmente C: no Windows ou / no Linux)
        try:
            if os.name == "nt":
                disco_principal = "C:\\"
            else:
                disco_principal = "/"

            info_disco = psutil.disk_usage(disco_principal)
            disco_livre = info_disco.free / (1024 ** 3)
            disco_percentual_livre = 100 - info_disco.percent

        except:
            try:
                particoes = psutil.disk_partitions()
                if particoes:
                    info_disco = psutil.disk_usage(particoes[0].mountpoint)
                    disco_livre = info_disco.free / (1024 ** 3)
                    disco_percentual_livre = 100 - info_disco.percent
                    disco_principal = particoes[0].mountpoint
                else:
                    disco_livre = 0
                    disco_percentual_livre = 0
                    disco_principal = "N/A"
            except:
                disco_livre = 0
                disco_percentual_livre = 0
                disco_principal = "N/A"

        # 4. REDE (taxa de download/upload)
        stats_rede = psutil.net_io_counters()
        bytes_recv_total = stats_rede.bytes_recv
        bytes_sent_total = stats_rede.bytes_sent

        # calcula a taxa se não é a primeira leitura
        if not primeira_leitura_rede:
            bytes_recv_delta = bytes_recv_total - bytes_recv_anterior
            bytes_sent_delta = bytes_sent_total - bytes_sent_anterior
            kb_s_recv = bytes_recv_delta / 1024
            kb_s_sent = bytes_sent_delta / 1024
        else:
            kb_s_recv = 0
            kb_s_sent = 0
            primeira_leitura_rede = False

        # guarda os valores para próxima iteração
        bytes_recv_anterior = bytes_recv_total
        bytes_sent_anterior = bytes_sent_total

        # ====== EXIBIÇÃO DO PAINEL ======

        limpar_tela()

        print("\n" + "=" * 70)
        print("              PAINEL DE MONITORAMENTO DE SISTEMA")
        print("=" * 70 + "\n")

        # SEÇÃO 1: MEMÓRIA RAM
        print("[MEMÓRIA RAM]")
        print("-" * 70)
        print(f"Uso:        {ram_percentual:>6.1f}% ({ram_usada:.2f} GB de {ram_total:.2f} GB usados)")

        barra_ram = "█" * int(ram_percentual / 5) + "░" * (20 - int(ram_percentual / 5))
        print(f"Barra:      [{barra_ram}]")

        if ram_percentual > 80:
            print("⚠️  ALERTA: RAM acima de 80%!")

        # SEÇÃO 2: CPU
        print("\n[PROCESSADOR]")
        print("-" * 70)
        print(f"Uso:        {cpu_percentual:>6.1f}%")

        barra_cpu = "█" * int(cpu_percentual / 5) + "░" * (20 - int(cpu_percentual / 5))
        print(f"Barra:      [{barra_cpu}]")

        # SEÇÃO 3: DISCO
        print("\n[DISCO]")
        print("-" * 70)
        print(f"Partição Principal: {disco_principal}")
        print(f"Espaço Livre:       {disco_livre:.2f} GB ({disco_percentual_livre:.1f}% disponível)")

        barra_disco = "█" * int((100 - disco_percentual_livre) / 5) + "░" * int(disco_percentual_livre / 5)
        print(f"Barra:              [{barra_disco}]")

        if disco_percentual_livre < 10:
            print("⚠️  ALERTA: Disco quase cheio!")

        # SEÇÃO 4: REDE
        print("\n[REDE]")
        print("-" * 70)
        print(f"Download:   {kb_s_recv:>10.2f} KB/s")
        print(f"Upload:     {kb_s_sent:>10.2f} KB/s")

        print("\n" + "=" * 70)
        print("Atualizando a cada 2 segundos...")
        print("Pressione Ctrl+C para interromper")
        print("=" * 70 + "\n")

        time.sleep(2)

except KeyboardInterrupt:
    limpar_tela()
    print("\n" + "=" * 70)
    print("Programa interrompido pelo usuário.")
    print("=" * 70 + "\n")

# Anotações:
# - Este exercício INTEGRA tudo que foi feito nos exercícios anteriores
# - Coleta dados de RAM (ex01), CPU (ex06), Disco (ex03), Rede (ex05)
# - os.name retorna "nt" para Windows ou "posix" para Linux/macOS
# - função limpar_tela() encapsula a lógica para deixar código mais limpo
# - try/except em torno do disco permite encontrar partição mesmo se a padrão falhar
# - primeira_leitura_rede é uma flag para não calcular delta na primeira vez
# - "█" e "░" são caracteres unicode para barra visual
# - int(percentual / 5) cria barra com 20 caracteres
# - loop infinito com time.sleep(2) atualiza a cada 2 segundos
# - try/except KeyboardInterrupt captura Ctrl+C e encerra limpamente