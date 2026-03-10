# Exercício 3 - Gerenciador de Espaço em Disco (Todas as Partições)

# importo psutil para acessar informações de disco
import psutil
import os

# limpo a tela
os.system("cls")

# exibo um título
print("="*90)
print("       GERENCIADOR DE ESPAÇO EM DISCO - TODAS AS PARTIÇÕES")
print("="*90)

# psutil.disk_partitions() retorna uma lista de todas as partições
# cada partição tem informações como device, mountpoint (ponto de montagem), fstype
particoes = psutil.disk_partitions()

# verifico se existem partições
if not particoes:
    print("Nenhuma partição encontrada!")
else:
    # criei uma variável para contar o número de partições
    # isso ajuda a saber quantas existem
    contador = 0

    # exibo o cabeçalho da tabela
    print(f"{'Partição':<15} {'Ponto Montagem':<20} {'Total':<15} {'Usado':<15} {'Livre':<15} {'Uso %':<10}")
    print("-" * 90)

    # loop para cada partição
    for particao in particoes:
        try:
            # obtenho o nome do device (ex: C:, /dev/sda1)
            device = particao.device

            # obtenho o ponto de montagem (C:, /, /home, etc)
            # mountpoint é onde a partição está "ligada" no sistema
            mountpoint = particao.mountpoint

            # psutil.disk_usage(ponto_montagem) retorna espaço total, usado, livre
            # isso retorna um objeto com atributos: total, used, free, percent
            info_disco = psutil.disk_usage(mountpoint)

            # extraio e converto para GB
            total_gb = info_disco.total / (1024 ** 3)
            usado_gb = info_disco.used / (1024 ** 3)
            livre_gb = info_disco.free / (1024 ** 3)
            percentual = info_disco.percent

            # exibo na tabela
            # {:15} significa: ocupa 15 caracteres, alinhado à esquerda
            # :.2f significa: 2 casas decimais após a vírgula
            print(f"{device:<15} {mountpoint:<20} {total_gb:>14.2f}GB {usado_gb:>14.2f}GB {livre_gb:>14.2f}GB {percentual:>9.1f}%")

            contador += 1

        except PermissionError:
            # algumas partições podem não ter permissão de leitura
            # quando isso acontece, informo e continuo com as próximas
            print(f"{device:<15} {mountpoint:<20} {'[Sem permissão]':<15} {'':<15} {'':<15} {'':<10}")

# exibo um rodapé com o total
print("-" * 90)
print(f"Total de partições: {contador}\n")

# Anotações:
# - psutil.disk_partitions() lista TODAS as partições do sistema
# - cada partição retorna: device (nome), mountpoint (onde está ligada), fstype (tipo)
# - psutil.disk_usage(caminho) retorna informações de um disco/partição específico
#   * total: espaço total em bytes
#   * used: espaço utilizado em bytes
#   * free: espaço livre em bytes
#   * percent: porcentagem de uso
# - try/except PermissionError trata quando não tenho permissão pra acessar uma partição
# - formatação de string com f-strings:
#   * {variavel:<15} alinha à esquerda, ocupa 15 caracteres
#   * {variavel:>15} alinha à direita, ocupa 15 caracteres
#   * {numero:.2f} mostra 2 casas decimais
# - (1024 ** 3) converte de bytes para GB
#   * 1024 bytes = 1 KB
#   * 1024^2 bytes = 1 MB
#   * 1024^3 bytes = 1 GB
