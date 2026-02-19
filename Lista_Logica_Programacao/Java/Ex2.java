// Exercício 2 - Soma de dois números

import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int num1 = sc.nextInt();

        System.out.print("Digite o segundo número: ");
        int num2 = sc.nextInt();

        int soma = num1 + num2;

        System.out.println("A soma é: " + soma);

        sc.close();
    }
}
/*
Anotações:

- Usei nextInt() porque é número inteiro.
- Java obriga declarar tipo antes.
*/