// Exercício 8 - Jogo de Adivinhação

import java.util.Random;
import java.util.Scanner;

public class Ex8 {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner sc = new Scanner(System.in);

        // sorteia número entre 1 e 100
        int numero = rand.nextInt(100) + 1;
        int tentativas = 0;

        while (true) {
            System.out.print("Digite um palpite (1-100): ");
            int palpite = sc.nextInt();
            tentativas++;

            if (palpite == numero) {
                System.out.println("Parabéns! Você acertou em " + tentativas + " tentativas.");
                break;
            } else if (palpite < numero) {
                System.out.println("Tente um número maior.");
            } else {
                System.out.println("Tente um número menor.");
            }
        }

        sc.close();
    }
}
/*
Anotações:

- Usei Random e Scanner; não esqueço de importar.
- rand.nextInt(100) retorna 0..99, por isso somo 1 para ficar 1..100.
- while(true) repete até o break quando acerta.
- contador de tentativas incrementa a cada laço.
- if/else com dicas maior/menor igual ao programa em Python.
- Scanner é fechado no final, sempre.
*/