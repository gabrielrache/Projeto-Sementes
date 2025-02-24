import java.util.Scanner;

public class Main {

    private static String leEntrada (String mensagem, Scanner teclado) {

        String entrada;

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

        Scanner scan = new Scanner(System.in);
        String usuario, senha;

        for (int tentativa = 1; tentativa <= 3; tentativa++) {

            usuario = leEntrada("Digite o nome de usuário: ", scan);
            senha = leEntrada("Digite a senha: ", scan);

            if (usuario.equals("aluno") && senha.equals("segredo")) {
                System.out.println("Bem vindo!");
                scan.close();
                System.exit(0);
            } else {
                System.out.println("Usuário e/ou Senha incorretos!");
            }
        }
        System.out.println("Login bloqueado - Excesso de tentativas");
        scan.close();
        System.exit(-1);
    }
}