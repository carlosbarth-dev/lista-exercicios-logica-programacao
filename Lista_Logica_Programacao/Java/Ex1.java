// Exercício 1 - Saudação

import java.util.Scanner; // Preciso importar para poder ler dados

public class Ex1 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in); // Criei objeto Scanner
        
        System.out.print("Digite seu nome: ");
        String nome = sc.nextLine(); // nextLine lê texto
        
        System.out.println("Olá, " + nome + "! Seja bem-vindo!");
        
        sc.close(); // sempre fechar o scanner
    }
}
/*
Anotações:

- Sempre preciso importar Scanner.
- Java precisa declarar tipo da variável (String).
- Tudo fica dentro de main.
- Precisa fechar o scanner no final.
*/