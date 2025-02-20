import java.util.Scanner;

public class Main {

    private static String leEntrada (String mensagem) {

        String entrada;
        Scanner teclado = new Scanner(System.in);

        while (true) {
            System.out.print(mensagem);

            try {
                entrada = teclado.next();
                break;
            } catch (Exception e) {
                System.out.println("Erro ao ler a entrada.");
            }
        }
        return entrada;
    }

    public static void main(String[] args) {

        String busca;
        String[] nomes = new String[10];

        for (int i = 0; i < 10; i++) {
            nomes[i] = leEntrada( "Digite um nome (" + (i+1) + "/10): ");
        }

        busca = leEntrada("Digite um nome para buscar no vetor: ");

        for (String nome : nomes){
            if(nome.equalsIgnoreCase(busca)){
                System.out.println("Achei");
                System.exit(0);
            }
        }
        System.out.println("Não achei");
    }
}