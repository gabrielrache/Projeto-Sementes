public class Main
{
    public static void main(String[] args)
    {
        int resultado = 0;

        for (int i = 1; i <= 100; i++ )
        {
            resultado += i;
        }

        System.out.printf("A soma dos números de 1 a 100 é: %d", resultado);
    }
}