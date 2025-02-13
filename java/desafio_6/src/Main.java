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
                    }
                    catch (Exception e) {
                        erro = teclado.next();
                        System.out.printf("%s não é um número inteiro!\n", erro);
                    }
                }
                while (true);

                if (leitura < val_a | leitura > val_b)
                    System.out.printf("%d não está entre %d e %d\n", leitura, val_a, val_b);
                else
                    break;
        } while (true);

        return leitura;
    }

    public static void main(String[] args)
    {
        int valor;

        do
        {
            valor = lerNumeroEntreAeB(1,10);

            if (valor == 10)
            {
                System.out.println("Encerramento do programa");
                break;
            }
        }
        while (true);
    }
}