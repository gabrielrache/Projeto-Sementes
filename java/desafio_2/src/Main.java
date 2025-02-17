import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        int quantidade;
        float desconto;
        float valor;
        float total;

        String nome;
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o nome do produto: ");
        nome = teclado.next();

        System.out.print("Digite a quantidade: ");
        quantidade = teclado.nextInt();

        System.out.print("Digite o valor: ");
        valor = teclado.nextFloat();

        if (quantidade > 50) {
            desconto = 25;
        } else if (quantidade > 20) {
            desconto = 20;
        } else if (quantidade > 10) {
            desconto = 10;
        } else {
            desconto = 0;
        }

        total = quantidade * valor * (1 - (desconto / 100));

        System.out.printf("Você comprou %d unidade(s) de %s por %.2f", quantidade, nome, total );
        if (desconto > 0)
            System.out.printf(" ganhando um desconto de %.0f%%!", desconto);
    }
}