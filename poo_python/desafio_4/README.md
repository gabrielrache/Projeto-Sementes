Desafio: Gerenciador de Biblioteca
Cenário: Você está desenvolvendo um sistema de gerenciamento de biblioteca. O sistema deve permitir que os usuários realizem as seguintes operações:

Adicionar Livro: O sistema deve permitir que um usuário adicione um novo livro à biblioteca, informando o título e o autor. Se o livro já existir na biblioteca, uma exceção deve ser lançada, e uma mensagem de erro deve ser exibida informando que o livro não pode ser adicionado novamente.

Emprestar Livro: O sistema deve permitir que um usuário empreste um livro. Se o livro não estiver disponível (já emprestado), uma exceção deve ser lançada, e uma mensagem de erro deve ser exibida informando que o livro não pode ser emprestado.

Devolver Livro: O sistema deve permitir que um usuário devolva um livro. Se o livro não foi emprestado anteriormente, uma exceção deve ser lançada, e uma mensagem de erro deve ser exibida informando que o livro não pode ser devolvido.

Requisitos:
Crie uma classe Livro com os atributos titulo, autor e disponivel.
Crie uma classe Biblioteca que gerencie uma lista de livros e implemente os métodos para adicionar, emprestar e devolver livros, tratando as exceções nas operações.
No método principal (main), teste as funcionalidades da classe Biblioteca, exibindo mensagens apropriadas para o usuário em cada operação.
Exemplos de Exceção: Em main, implemente um exemplo de exceção para cada um dos três métodos (adicionarLivro, emprestarLivro e devolverLivro), utilizando blocos try-catch para capturar e tratar as exceções lançadas.