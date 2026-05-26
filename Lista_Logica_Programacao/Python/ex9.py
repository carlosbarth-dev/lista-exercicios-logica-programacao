# Exercício 9 - Calculadora Simples

# programa que mostra um menu e realiza operações básicas
# o usuário escolhe a operação, insere dois números e o resultado é exibido

while True:
    # mostra o menu de opções
    print("\n=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = input("Escolha a operação (1-5): ")

    if escolha == "5":
        print("Saindo...")
        break  # encerra o loop

    # pede os números; converto para float para aceitar décimais
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # verifica qual operação fazer
    if escolha == "1":
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")
    elif escolha == "2":
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif escolha == "3":
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    elif escolha == "4":
        # cuidado com divisão por zero
        if num2 == 0:
            print("Erro: divisão por zero!")
        else:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
    else:
        print("Opção inválida, tente novamente.")

# Anotações:
# - usei while True para que o menu volte até o usuário escolher sair.
# - input() retorna string, por isso comparo escolha com "1", "2" etc.
# - converti os números para float porque podem ser com ponto.
# - if/elif/else verificam a operação escolhida.
# - cuidei da divisão por zero para não gerar erro.
# - coloquei comentários e notas como nos outros exercícios, explicando cada parte para revisar com o professor.