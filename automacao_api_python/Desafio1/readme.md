### Desafio: Testando Endpoints de API com a Biblioteca Requests e Pytest

Neste desafio, você deverá interagir com os principais endpoints da API **PetStore** utilizando a biblioteca `requests` e `Pytest`. O objetivo é realizar requisições HTTP (POST, GET, PUT, DELETE) e validar as respostas recebidas, garantindo que cada operação esteja funcionando corretamente através de assertivas adequadas.
Deve ser criado um método para cada teste descrito abaixo.  

### Documentação da API
Você utilizará a seguinte documentação da API: [PetStore API](https://petstore.swagger.io/)

### Endpoints a serem testados:

### 1. POST: Criar Usuário

- **Endpoint**: `/user/create`
- **Descrição**: Validação da criação um usuário com as informações dadas.
- **Tarefa**: Realizar uma requisição POST enviando um usuário, incluindo todos os campos necessários. O campo `id` deve ser deixado com `0`. A resposta do endpoint deve ser validada, garantindo que:
  - O código de status retornado seja **200 OK**.
  - O corpo da resposta contenha as informações corretas do usuário criado.
  - Não precisa validar o ID retornado pois esse será sempre diferente do informado.


### 2. GET: Obter Usuário

- **Endpoint**: `/user/{username}`
- **Descrição**: Obtém os detalhes usuário pelo username
- **Tarefa**: Realizar uma requisição GET fornecendo o nome de um usuário e validar se os detalhes retornados estão corretos. A resposta do endpoint deve ser validada, garantindo que:
  - O código de status retornado seja **200 OK**.
  - O corpo da resposta contenha as informações do usuário corretas.


### 3. PUT: Atualizar Usuário

- **Endpoint**: `/user/{username}`
- **Descrição**: Atualiza os detalhes de um usuário existente.
- **Tarefa**: Realizar uma requisição PUT para atualizar as informações de um usuário e validar se as mudanças foram aplicadas com sucesso. A resposta do endpoint deve ser validada, garantindo que:
  - O código de status retornado seja **200 OK**.

### 4. DELETE: Excluir Usuário

- **Endpoint**: `/user/{username}`
- **Descrição**: Remove um usuário com base no nome de usuário fornecido.
- **Tarefa**: Realizar uma requisição DELETE para excluir um usuário e verificar se ele foi removido corretamente. A resposta do endpoint deve ser validada, garantindo que:
  - O código de status retornado seja **200 OK**.

