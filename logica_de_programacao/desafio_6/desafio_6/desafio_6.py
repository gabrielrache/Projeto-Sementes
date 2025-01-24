"""Lê entradas do usuário até que seja enviado '10', encerrando a execução"""

while True:
    guess = float(input('Digite qualquer número. Para sair, digite 10: '))
    
    if guess == 10:
        break