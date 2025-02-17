import java.util.Scanner;

public class Main {

    private static int lerNumeroEntreAeB(int val_a, int val_b) {

        int leitura;
        String erro;

        Scanner teclado = new Scanner(System.in);

        do {
            do {
                System.out.printf("Digite um número inteiro entre %d a %d: ", val_a, val_b);

                try {
                    leitura = teclado.nextInt();
                    break;
                } catch (Exception e) {
                    erro = teclado.next();
                    System.out.printf("%s não é um número inteiro!\n", erro);
                }
            } while (true);

            if (leitura < val_a || leitura > val_b)
                System.out.printf("%d não está entre %d e %d\n", leitura, val_a, val_b);
            else
                break;
        } while (true);

        return leitura;
    }

    public static void main(String[] args) {

        int numero = lerNumeroEntreAeB(1,10);
        int resultado;

        for (int i = 1; i <= 10; i++) {
            if (i == 1)
                System.out.printf("Tabuada do %d:\n", numero);

            resultado = i * numero;

            System.out.printf("%d x %d = %d\n", numero, i, resultado);
        }
    }
}