import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner teclado = new Scanner(System.in);
        String nome;
        float valor = 0;
        float comissao;

        System.out.print ("Digite o nome do vendedor: ");
        nome = teclado.next();

        try
        {
            System.out.print("Digite o valor do imóvel: ");
            valor = teclado.nextFloat();
        }
        catch (Exception e)
        {
            System.out.println("Valor inválido");
            System.exit(-1);
        }

        if (valor >= 50000)
        {
            comissao = valor * 20 / 100;
        } else if (valor >= 30000)
        {
            comissao = valor * 15 / 100;
        }
        else
        {
            comissao = valor * 10 / 100;
        }

        System.out.printf("%s, a comissão de venda pelo imóvel de R$ %.2f é de R$ %.2f", nome, valor, comissao);
    }
}