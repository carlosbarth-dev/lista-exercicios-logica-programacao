// Exercício 6 - Contar o número de vogais em uma frase

import java.util.Scanner;

public class Ex6 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String frase = sc.nextLine();

        int contador = 0;

        for (int i = 0; i < frase.length(); i++) {
            char letra = frase.charAt(i);

            if ("aeiouAEIOU".indexOf(letra) != -1) {
                contador++;
            }
        }

        System.out.println("Quantidade de vogais: " + contador);

        sc.close();
    }
}
/*
Anotações:

- Usei frase.length() para saber o tamanho da string
- Usei charAt(i) para pegar letra por letra
- Usei indexOf para verificar se a letra existe dentro da string de vogais
- Se indexOf retornar diferente de -1, significa que encontrou
- Java exige mais código para manipular string
*/