#language: pt

  Funcionalidade: automatizar testes da petstore

    Contexto:
      Dado que estou usando a api da petstore

    Cenario: Criar usuários a partir de lista
      Dado que tenho uma lista de usuários
      Quando cadastro os usuários através da opção de lista
      Então haverá retorno 200
      E haverá mensagem "ok" no corpo

    Cenario: Obter detalhes do usuário
      Dado que tenho um usuário cadastrado
      Quando buscar as informações do usuario
      Então haverá retorno 200
      E os dados retornarão no corpo

    Cenario: Atualiza os detalhes de um usuário existente
      Dado que tenho um usuário cadastrado
      E tenho as novas informações para atualizar
      Quando atualizo as informações
      Então haverá retorno 200

    Cenario: Remove um usuário com base no nome de usuário fornecido
      Dado que tenho um usuário cadastrado
      Quando removo o usuário
      Então haverá retorno 200