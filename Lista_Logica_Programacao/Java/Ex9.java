// Exercício 9 - Calculadora Simples com Métodos

import java.util.Scanner;

public class Ex9 {
    // métodos estáticos para cada operação
    // cada método recebe dois números e retorna o resultado

    public static double somar(double a, double b) {
        return a + b;
    }

    public static double subtrair(double a, double b) {
        return a - b;
    }

    public static double multiplicar(double a, double b) {
        return a * b;
    }

    // método dividir com if/else para cuidar de divisão por zero
    public static Double dividir(double a, double b) {
        if (b == 0) {
            return null;  // retorna null se não conseguir dividir
        } else {
            return a / b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n=== Calculadora ===");
            System.out.println("1 - Soma");
            System.out.println("2 - Subtração");
            System.out.println("3 - Multiplicação");
            System.out.println("4 - Divisão");
            System.out.println("5 - Sair");

            System.out.print("Escolha a operação (1-5): ");
            int escolha = sc.nextInt();

            if (escolha == 5) {
                System.out.println("Saindo...");
                break;
            }

            System.out.print("Digite o primeiro número: ");
            double num1 = sc.nextDouble();
            System.out.print("Digite o segundo número: ");
            double num2 = sc.nextDouble();

            // verifica qual operação fazer e chama o método apropriado
            if (escolha == 1) {
                double resultado = somar(num1, num2);  // chama método somar
                System.out.println("Resultado da soma: " + resultado);
            } else if (escolha == 2) {
                double resultado = subtrair(num1, num2);  // chama método subtrair
                System.out.println("Resultado da subtração: " + resultado);
            } else if (escolha == 3) {
                double resultado = multiplicar(num1, num2);  // chama método multiplicar
                System.out.println("Resultado da multiplicação: " + resultado);
            } else if (escolha == 4) {
                Double resultado = dividir(num1, num2);  // chama método dividir
                if (resultado == null) {
                    System.out.println("Erro: divisão por zero!");
                } else {
                    System.out.println("Resultado da divisão: " + resultado);
                }
            } else {
                System.out.println("Opção inválida, tente novamente.");
            }
        }

        sc.close();
    }
}
/*
Anotações:

- public static é necessário para criar métodos que a main pode chamar.
- return devolve o resultado do método quando ele é chamado.
- cada método (somar, subtrair, multiplicar, dividir) faz uma operação.
- Double (com D maiúsculo) permite retornar null para erro na divisão.
- if/elif/else escolhem qual método chamar conforme a opção.
- métodos deixam o código mais organizado e reutilizável.
- null significa "sem valor", usado para indicar erro na divisão.
*/