// Exercício 5 - Verificar se um número é par ou ímpar

import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        if (numero % 2 == 0) {
            System.out.println("É par");
        } else {
            System.out.println("É ímpar");
        }

        sc.close();
    }
}
/*
Anotações:

- % funciona igual no Java
- Precisa usar parênteses na condição do if
- Java exige chaves {} mesmo se for uma linha
- Estrutura é mais rígida que Python
*/