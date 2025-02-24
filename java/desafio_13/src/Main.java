import java.util.Scanner;

public class Main {

    private static String leEntrada (String mensagem, Scanner teclado) {

        String entrada;

        while (true) {
            System.out.print(mensagem);

            try {
                entrada = teclado.nextLine();
                break;
            } catch (Exception e) {
                System.out.println("Erro ao ler a entrada.");
            }
        }
        return entrada;
    }

    public static void main(String[] args) {

        String busca;
        Scanner scan = new Scanner(System.in);
        String[] nomes = new String[10];

        for (int i = 0; i < 10; i++) {
            String msg = "Digite um nome (" + (i+1) + "/10): ";
            nomes[i] = leEntrada(msg, scan);
        }

        busca = leEntrada("Digite um nome para buscar no vetor: ", scan);

        for (String nome : nomes){
            if(nome.equalsIgnoreCase(busca)){
                System.out.println("Achei");
                System.exit(0);
            }
        }
        System.out.println("Não achei");
        scan.close();
    }
}