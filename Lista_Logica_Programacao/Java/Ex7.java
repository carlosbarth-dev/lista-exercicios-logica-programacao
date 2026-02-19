// Exercício 7 - Maior, menor e média de uma lista de números

import java.util.Scanner;

public class Ex7 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números? ");
        int quantidade = sc.nextInt();

        double[] numeros = new double[quantidade];

        for (int i = 0; i < quantidade; i++) {
            numeros[i] = sc.nextDouble();
        }

        double maior = numeros[0];
        double menor = numeros[0];
        double soma = 0;

        for (int i = 0; i < quantidade; i++) {
            if (numeros[i] > maior) {
                maior = numeros[i];
            }
            if (numeros[i] < menor) {
                menor = numeros[i];
            }
            soma += numeros[i];
        }

        double media = soma / quantidade;

        System.out.println("Maior: " + maior);
        System.out.println("Menor: " + menor);
        System.out.println("Média: " + media);

        sc.close();
    }
}
/*
Anotações:

- Usei array porque preciso armazenar vários valores
- double[] numeros cria vetor com tamanho definido
- Precisei iniciar maior e menor com o primeiro valor do array
- Fiz um segundo for para comparar manualmente
- Java não tem max() e min() prontos para array simples
- Precisei calcular soma manualmente
*/