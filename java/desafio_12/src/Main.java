import java.util.Scanner;

public class Main {

    private static int leInteiro (String mensagem){

        int leitura;
        String erro;
        Scanner teclado = new Scanner(System.in);

        while (true) {
            try {
                System.out.print(mensagem);
                leitura = teclado.nextInt();
                break;

            } catch (Exception e) {
                erro = teclado.next();
                System.out.println(erro + " não é um inteiro válido");
            }
        }
        return leitura;
    }

    public static void main(String[] args) {

        int qtdImpar = 0;

        int[] vetor = new int[10];

        for (int i = 0; i < 10; i++){
            vetor[i] = leInteiro( "Digite um inteiro (" + (i+1) + "/10): ");
        }

        for (int valor : vetor) if ((valor % 2) == 1) qtdImpar++;
        System.out.println("Quantidade de valores ímpares no vetor: " + qtdImpar);
    }
}