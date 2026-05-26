// Exercício 10 - Gerenciador de Tarefas

import java.util.Scanner;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Ex10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n=== Gerenciador de Tarefas ===");
            System.out.println("1 - Adicionar tarefa");
            System.out.println("2 - Listar tarefas");
            System.out.println("3 - Sair");

            System.out.print("Escolha uma opção (1-3): ");
            int escolha = sc.nextInt();
            sc.nextLine();  // consome a quebra de linha

            if (escolha == 3) {
                System.out.println("Saindo...");
                break;
            }

            // opção 1: adicionar tarefa
            if (escolha == 1) {
                System.out.print("Digite a tarefa: ");
                String tarefa = sc.nextLine();

                try {
                    // FileWriter com true abre em modo append (adicionar)
                    FileWriter arquivo = new FileWriter("tarefas.txt", true);
                    // escrevo a tarefa no arquivo
                    arquivo.write(tarefa + "\n");
                    // sempre fechar o arquivo depois de usar
                    arquivo.close();
                    System.out.println("Tarefa adicionada com sucesso!");

                } catch (IOException e) {
                    System.out.println("Erro ao salvar a tarefa!");
                }
            }

            // opção 2: listar tarefas
            else if (escolha == 2) {
                try {
                    // FileReader para ler o arquivo
                    FileReader fileReader = new FileReader("tarefas.txt");
                    // BufferedReader facilita ler linha por linha
                    BufferedReader leitor = new BufferedReader(fileReader);

                    System.out.println("\n=== Tarefas ===");
                    String linha;
                    int numero = 1;

                    // readLine() lê uma linha por vez até chegar ao fim (null)
                    while ((linha = leitor.readLine()) != null) {
                        System.out.println(numero + " - " + linha);
                        numero++;
                    }

                    leitor.close();
                    fileReader.close();

                } catch (IOException e) {
                    System.out.println("Nenhuma tarefa ainda. Adicione uma primeiro!");
                }
            }

            else {
                System.out.println("Opção inválida, tente novamente.");
            }
        }

        sc.close();
    }
}
/*
Anotações:

- FileWriter é usado para escrever em arquivo.
- new FileWriter("tarefas.txt", true) abre em modo append (true = adicionar).
- FileReader é usado para ler arquivo.
- BufferedReader facilita leitura linha por linha.
- write() escreve texto no arquivo.
- readLine() lê uma linha do arquivo, retorna null quando chega ao fim.
- close() sempre fechar o arquivo depois de usar.
- try/catch trata erros como arquivo não encontrado.
- IOException é a exceção lançada em operações de arquivo.
- a variável numero conta as tarefas manualmente neste caso.
*/
