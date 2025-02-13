import java.util.Scanner;

public class Main {

    private static int leNumerador(){

        Scanner teclado = new Scanner(System.in);

        int valor;
        String erro;

        do {
            System.out.print("Digite o numerador: ");

            try {
                valor = teclado.nextInt();
                break;
            }
            catch (Exception e) {
                erro = teclado.next();
                System.out.printf("%s não é um numerador válido!\n", erro);
            }
        }
        while (true);

        return valor;
    }

    private static int leDenominador() {

        Scanner teclado = new Scanner(System.in);

        int valor;
        String erro;

        do {
            do {
                System.out.print("Digite o denominador: ");

                try {
                    valor = teclado.nextInt();
                    break;
                } catch (Exception e) {
                    erro = teclado.next();
                    System.out.printf("%s não é um número válido!\n", erro);
                }
            }
            while (true);

            if (valor == 0)
                System.out.println("Digite um denominador válido!");
            else
                break;

        } while (true);
        return valor;
    }

    public static void main(String[] args) {

        int numerador, denominador;
        int quociente, resto;

        numerador = leNumerador();
        denominador = leDenominador();

        quociente = numerador / denominador;
        resto = numerador % denominador;

        System.out.printf("O quociente da divisão de %d por %d é %d. O resto da divisão é %d", numerador, denominador, quociente, resto);
    }
}