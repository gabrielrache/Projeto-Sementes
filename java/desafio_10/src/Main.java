import java.util.Scanner;
import static java.lang.Math.abs;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        while (true) {

            float[] notas = new float[2];
            int n = 0;

            while (n < 2) {

                System.out.printf("Digite a nota %d: ", (n + 1));

                try {
                    notas[n] = teclado.nextFloat();

                    if (notas[n] < 0) {
                        System.out.println("Número negativo detectado e convertido para positivo!");
                        notas[n] = abs(notas[n]);
                    }
                    n++;

                } catch (Exception e) {
                    String erro = teclado.nextLine();
                    System.out.printf("%s não é uma nota válida!\n", erro);
                }
            }

            float media = 0;

            for (float nota : notas) {
                media += nota;
            }

            media = media/notas.length;

            System.out.printf("A Média do aluno é %.2f. ", media);
            if (media < 7)
                System.out.println("O aluno foi reprovado.");
            else
                System.out.println("O aluno foi aprovado!");

            String continuar;

            do{
                System.out.println("Realizar novo cálculo (S/N)? ");
                continuar = teclado.next();

                if (continuar.equalsIgnoreCase("N")) {
                    teclado.close();
                    System.out.println(continuar);
                    System.exit(0);
                }
            } while (!continuar.equalsIgnoreCase("S"));
        }
    }
}