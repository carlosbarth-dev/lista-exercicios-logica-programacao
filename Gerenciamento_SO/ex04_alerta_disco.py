# Exercício 4 - Alerta de Pouco Espaço em Disco

# este exercício reutiliza a lógica do exercício 3
# mas com um foco em alertas para partições críticas

import psutil
import os

# limpo a tela
os.system("cls")

# exibo um título
print("="*70)
print("       ALERTA DE POUCO ESPAÇO EM DISCO")
print("="*70)

# leio do usuário o limite crítico (em %)
# por exemplo: se a partição tem menos de 10% livre, é alerta
limite_critico = float(input("Digite o limite crítico de espaço livre (%): "))

# calculo o percentual inverso
# se limite_critico é 10 (livre), então 90 (usado) é o alerta
limite_uso = 100 - limite_critico

print("\n" + "="*70)
print(f"Partições com menos de {limite_critico}% de espaço livre:\n")
print("="*70)

# obtenho todas as partições (igual ao ex3)
particoes = psutil.disk_partitions()

# variável para contar alertas
alertas = 0

# loop para cada partição
for particao in particoes:
    try:
        device = particao.device
        mountpoint = particao.mountpoint

        # obtenho as informações de uso de disco
        info_disco = psutil.disk_usage(mountpoint)

        # extraio as informações
        total_gb = info_disco.total / (1024 ** 3)
        usado_gb = info_disco.used / (1024 ** 3)
        livre_gb = info_disco.free / (1024 ** 3)
        percentual_uso = info_disco.percent
        percentual_livre = 100 - percentual_uso

        # verifico se está na zona crítica
        if percentual_livre <= limite_critico:
            print(f"\n⚠️  {device} ({mountpoint})")
            print(f"   Espaço total:     {total_gb:.2f} GB")
            print(f"   Espaço usado:     {usado_gb:.2f} GB ({percentual_uso:.1f}%)")
            print(f"   Espaço livre:     {livre_gb:.2f} GB ({percentual_livre:.1f}%)")
            print(f"   Status: CRÍTICO - menos de {limite_critico}% disponível")
            alertas += 1

    except PermissionError:
        pass

print("\n" + "="*70)
if alertas == 0:
    print("✓ Nenhuma partição em estado crítico!")
else:
    print(f"⚠️  Total de partições em alerta: {alertas}")
print("="*70)

# Anotações:
# - este exercício REUTILIZA o código do ex3
# - mostra apenas partições críticas
# - percentual_livre = 100 - percentual_uso
# - try/except protege contra partições sem permissão