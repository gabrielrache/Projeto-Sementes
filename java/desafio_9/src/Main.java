import java.util.Scanner;

public class Main {

    public static int leNumerador(Scanner teclado){

        int valor;
        String erro;

        while (true) {
            System.out.print("Digite o numerador: ");

            try {
                valor = teclado.nextInt();
                break;
            } catch (Exception e) {
                erro = teclado.nextLine();
                System.out.printf("%s não é um numerador válido!\n", erro);
            }
        }
        return valor;
    }

    private static int leDenominador (Scanner teclado) {

        int valor;
        String erro;

        while (true) {
            while (true) {
                System.out.print("Digite o denominador: ");

                try {
                    valor = teclado.nextInt();
                    break;
                } catch (Exception e) {
                    erro = teclado.nextLine();
                    System.out.printf("%s não é um número válido!\n", erro);
                }
            }

            if (valor == 0)
                System.out.println("Digite um denominador válido!");
            else
                break;

        }
        return valor;
    }

    public static void main(String[] args) {

        int numerador, denominador;
        int quociente, resto;

        Scanner scan = new Scanner(System.in);

        numerador = leNumerador(scan);
        denominador = leDenominador(scan);

        quociente = numerador / denominador;
        resto = numerador % denominador;

        System.out.printf("O quociente da divisão de %d por %d é %d. O resto da divisão é %d", numerador, denominador, quociente, resto);

        scan.close();
    }
}