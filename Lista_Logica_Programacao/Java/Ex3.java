// Exercício 3 - Média de três números

import java.util.Scanner;

public class Ex3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double n1 = sc.nextDouble();
        double n2 = sc.nextDouble();
        double n3 = sc.nextDouble();

        double media = (n1 + n2 + n3) / 3;

        System.out.println("A média é: " + media);

        sc.close();
    }
}
/*
Anotações:

- Usei double porque a média pode gerar número quebrado
- nextDouble() lê números decimais
- A fórmula da média é (n1 + n2 + n3) / 3
- Em Java, se eu usasse int poderia perder a parte decimal
- Declarei todas as variáveis antes de usar (Java exige tipo)
- Sempre preciso fechar o Scanner no final com sc.close()
*/
