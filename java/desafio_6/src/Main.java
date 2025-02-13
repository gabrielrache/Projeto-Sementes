import java.util.Scanner;

public class Main
{
    private static int lerNumero()
    {
        int leitura;
        String erro;

        Scanner teclado = new Scanner(System.in);

        do
        {
            System.out.print("Digite um número inteiro entre 1 a 10: ");

            try
            {
                leitura = teclado.nextInt();
                break;
            }
            catch (Exception e)
            {
                erro = teclado.next();
                System.out.printf("%s não é um número inteiro!\n", erro);
            }
        }
        while (true);

        return leitura;
    }

    public static void main(String[] args)
    {
        int valor;

        do
        {
            do
            {
                valor = lerNumero();

                if (valor <1 | valor > 10)
                    System.out.printf("%d não está entre 1 e 10\n", valor);

                else break;
            }
            while (true);

            if (valor == 10)
            {
                System.out.println("Encerramento do programa");
                break;
            }
        }
        while (true);
    }
}