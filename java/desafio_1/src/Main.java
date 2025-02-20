import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        String produto;
        int idade;

        Scanner teclado = new Scanner(System.in);

        System.out.print("""
                Produtos disponíveis:
                1 - água
                2 - refrigerante
                3 - cerveja
                
                Digite a nome ou a opção desejada:\s""");

        produto = teclado.next();

        if (produto.equals("3") || produto.equalsIgnoreCase("cerveja")) {

            System.out.print("Digite a sua idade: ");
            idade = teclado.nextInt();

            if (idade >= 18)
                System.out.println("Compra efetuada com sucesso");
            else
                System.out.println("compra negada");

        } else if (produto.equals("1") || produto.equals("2") || produto.equalsIgnoreCase("refrigerante") || produto.equalsIgnoreCase("água") || produto.equalsIgnoreCase("agua"))
            System.out.println("Compra efetuada com sucesso!");
        else
            System.out.println("produto não encontrado");
    }
}