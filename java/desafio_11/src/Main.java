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

        String usuario, senha;

        for (int tentativa = 1; tentativa <= 3; tentativa++) {

            usuario = leEntrada("Digite o nome de usuário: ");
            senha = leEntrada("Digite a senha: ");

            if (usuario.equals("aluno") && senha.equals("segredo")) {
                System.out.println("Bem vindo!");
                System.exit(0);
            } else {
                System.out.println("Usuário e/ou Senha incorretos!");
            }
        }
        System.out.println("Login bloqueado - Excesso de tentativas");
        System.exit(-1);
    }
}