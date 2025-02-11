import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {

        Scanner teclado = new Scanner(System.in);

        float total = 0;
        float valor_1;
        float valor_2;
        String oper;


        while (true)
        {
            System.out.print("Digite o primeiro número: ");
            try
            {
                valor_1 = teclado.nextFloat();
                break;
            }
            catch (Exception e)
            {
                System.out.println("Digite um número válido!");
                teclado.next();
            }
        }

        while (true) {
            System.out.print("Digite o operador matemático: ");
            oper = teclado.next();

            if (oper.equalsIgnoreCase("mais") | oper.equalsIgnoreCase("soma"))
            {
                oper = "+";
                break;
            }
            else if (oper.equalsIgnoreCase("menos") | oper.equalsIgnoreCase("subtração"))
            {
                oper = "-";
                break;
            }
            else if (oper.equalsIgnoreCase("x") | oper.equalsIgnoreCase("multiplicação") | oper.equalsIgnoreCase("vezes"))
            {
                oper = "*";
                break;
            }
            else if (oper.equals(":") | oper.equalsIgnoreCase("divisão"))
            {
                oper = "/";
                break;
            }
            else
            {
                System.out.println("Digite um operador válido!");
            }
        }


        while (true)
        {
            System.out.print("Digite o segundo número: ");
            try
            {
                valor_2 = teclado.nextFloat();

                if (valor_2 == 0)
                {
                    System.out.println("Não é possível dividir por zero!");
                }
                else
                {
                    break;
                }
            }
            catch (Exception e)
            {
                System.out.println("Digite um número válido!");
                teclado.next();
            }
        }



        switch (oper)
        {
            case "+":
                total = valor_1 + valor_2;
                break;
            case "-":
                total = valor_1 - valor_2;
                break;
            case "*":
                total = valor_1 * valor_2;
                break;
            case "/":
                total = valor_1 / valor_2;
                break;
            default:
                System.out.println("Não foi inserida uma operação válida. Tente novamente");
        }

        System.out.printf("Resultado: %.2f", total);
    }
}