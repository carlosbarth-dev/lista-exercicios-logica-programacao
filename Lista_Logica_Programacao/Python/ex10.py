# Exercício 10 - Gerenciador de Tarefas

# programa que permite adicionar e listar tarefas em um arquivo de texto

while True:
    # mostra o menu de opções
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    escolha = input("Escolha uma opção (1-3): ")

    if escolha == "3":
        print("Saindo...")
        break

    # opção 1: adicionar tarefa
    if escolha == "1":
        tarefa = input("Digite a tarefa: ")
        # open com "a" abre o arquivo em modo append (adicionar)
        arquivo = open("tarefas.txt", "a")
        # escrevo a tarefa no arquivo
        arquivo.write(tarefa + "\n")
        # sempre fechar o arquivo depois de usar
        arquivo.close()
        print("Tarefa adicionada com sucesso!")

    # opção 2: listar tarefas
    elif escolha == "2":
        try:
            # open com "r" abre em modo read (leitura)
            arquivo = open("tarefas.txt", "r")
            # read() lê todo o conteúdo do arquivo
            conteudo = arquivo.read()
            arquivo.close()

            # split("\n") divide o texto por quebras de linha
            tarefas = conteudo.split("\n")

            print("\n=== Tarefas ===")
            # enumerate() numera automaticamente cada item da lista
            for numero, tarefa in enumerate(tarefas, 1):
                # só mostra se a tarefa não estiver vazia
                if tarefa:
                    print(f"{numero} - {tarefa}")

        except FileNotFoundError:
            # erro caso o arquivo não exista ainda
            print("Nenhuma tarefa ainda. Adicione uma primeiro!")

    else:
        print("Opção inválida, tente novamente.")

# Anotações:
# - open("arquivo.txt", "a") abre o arquivo em modo append para adicionar linhas.
# - open("arquivo.txt", "r") abre em modo read para ler o conteúdo.
# - sempre usar arquivo.close() depois de usar o arquivo.
# - write() escreve texto no arquivo.
# - read() lê todo o conteúdo como uma string.
# - split("\n") divide a string em uma lista usando a quebra de linha como separador.
# - enumerate() retorna índice e valor simultaneamente, começando do 1 neste caso.
# - try/except trata erros, como quando o arquivo não existe ainda.
# - if tarefa: verifica se a tarefa não está vazia antes de exibir.