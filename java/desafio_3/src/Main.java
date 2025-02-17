import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        float nota = 0;
        float media;

        Scanner teclado = new Scanner(System.in);

        for (int n =1; n <= 3; n++) {
            System.out.printf("Digite a nota %d: ", n);
            nota += teclado.nextFloat();
        }

        media = nota/3;

        System.out.printf("\nMédia final: %.1f. ", media);

        if (media >= 7)
            System.out.println("Aprovado");
        else if (media >= 5)
            System.out.println("Recuperação");
        else
            System.out.println("Reprovado");
    }
}