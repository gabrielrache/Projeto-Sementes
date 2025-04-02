'''Módulo da classe principal'''

import sys
import ui

from biblioteca import Biblioteca as bib

bib.inicializar_acervo()

continuar = True

while continuar:
    ui.imprimir_menu_principal()
    op = None

    try:
        try:
            op = int(input("Selecione a opção desejada: "))

            if not 0 <= op < 5:
                raise Exception

        except Exception:
            print("Digite uma opção válida!")

        match op:
            case 1:
                ui.imprimir_menu_inclusao()
                mensagem = bib.adicionar_livro(bib.criar_livro())
                print(mensagem)
                input("Tecle ENTER para continuar...")

            case 2:
                ui.imprimir_menu_busca()

                loop_leitura = True

                while loop_leitura:
                    try:
                        sub = int(input("Selecione a opção desejada: "))

                        if not 0 <= sub < 4:
                            raise Exception

                        loop_leitura = False

                    except Exception:
                        print("Digite uma opção válida!")

                if 0 < sub < 4:
                    ui.imprimir_menu_busca_listar(sub)
                    bib.imprimir_busca(bib.localizar_livros(sub))
                    input("Tecle ENTER para continuar...")

            case 3:
                livros = bib.localizar_tudo()

                if len(livros) == 0:
                    print("Não há livros para exibir.")
                    input("Tecle ENTER para continuar...")
                    break

                ui.imprimir_menu_emprestar()

                bib.imprimir_busca(livros)

                loop_leitura = True

                while loop_leitura:
                    try:
                        sub = int(input("Digite o Número do livro desejado: "))

                        if not 0 < sub < len(livros):
                            raise Exception

                        loop_leitura = False

                    except Exception:
                        print("Digite uma opção válida!")

                sub -= 1

                bib.emprestar_livro(livros[sub])
                input("Tecle ENTER para continuar...")

            case 4:
                livros = bib.localizar_tudo()

                if len(livros) == 0:
                    print("Não há livros para exibir.")
                    input("Tecle ENTER para continuar...")
                    break

                ui.imprimir_menu_devolver()

                bib.imprimir_busca(livros)

                loop_leitura = True

                while loop_leitura:
                    try:
                        sub = int(input("Digite o Número do livro desejado: "))

                        if not 0 < sub < len(livros):
                            raise Exception

                        loop_leitura = False

                    except Exception:
                        print("Digite uma opção válida!")

                sub -= 1

                bib.devolver_livro(livros[sub])
                input("Tecle ENTER para continuar...")


            case 0:
                continuar = False

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário!")
        sys.exit(0)

print("\nFim da execução")
sys.exit(0)
