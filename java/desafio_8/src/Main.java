import java.util.Scanner;

public class Main {

    private static int lerNumeroEntreAeB(int val_a, int val_b, Scanner teclado) {

        int leitura;
        String erro;

        while (true) {
            while (true) {
                System.out.printf("Digite um número inteiro entre %d a %d: ", val_a, val_b);

                try {
                    leitura = teclado.nextInt();
                    break;
                } catch (Exception e) {
                    erro = teclado.nextLine();
                    System.out.printf("%s não é um número inteiro!\n", erro);
                }
            }

            if (leitura < val_a || leitura > val_b)
                System.out.printf("%d não está entre %d e %d\n", leitura, val_a, val_b);
            else
                break;
        }
        return leitura;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int numero = lerNumeroEntreAeB(1,10, scan);
        int resultado;

        for (int i = 1; i <= 10; i++) {
            if (i == 1)
                System.out.printf("Tabuada do %d:\n", numero);

            resultado = i * numero;

            System.out.printf("%d x %d = %d\n", numero, i, resultado);

            scan.close();
        }
    }
}