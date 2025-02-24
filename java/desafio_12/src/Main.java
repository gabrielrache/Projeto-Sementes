import java.util.Scanner;

public class Main {

    private static int leInteiro (String mensagem, Scanner teclado){

        int leitura;
        String erro;

        while (true) {
            try {
                System.out.print(mensagem);
                leitura = teclado.nextInt();
                break;

            } catch (Exception e) {
                erro = teclado.nextLine();
                System.out.println(erro + " não é um inteiro válido");
            }
        }
        return leitura;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int qtdImpar = 0;

        int[] vetor = new int[10];

        for (int i = 0; i < 10; i++){

            String msg = "Digite um inteiro (" + (i+1) + "/10): ";
            vetor[i] = leInteiro(msg, scan);
        }

        for (int valor : vetor) if ((valor % 2) == 1) qtdImpar++;
        System.out.println("Quantidade de valores ímpares no vetor: " + qtdImpar);

        scan.close();
    }
}