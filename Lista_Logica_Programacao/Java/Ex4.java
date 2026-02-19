// Exercício 4 - Tabuada de um número

import java.util.Scanner;

public class Ex4 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + " x " + i + " = " + (numero * i));
        }

        sc.close();
    }
}
/*
Anotações:

- Usei for tradicional porque Java precisa declarar a variável do contador
- int i = 1 começa no 1
- i <= 10 faz repetir até 10
- i++ incrementa de 1 em 1
- Precisei colocar (numero * i) entre parênteses porque senão ele poderia concatenar errado com string
*/