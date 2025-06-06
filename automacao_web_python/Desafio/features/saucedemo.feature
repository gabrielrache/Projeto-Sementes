#language: en

Feature: Saucedemo

Background:
Given que acesso o site saucedemo

#Realizar login e validar que esta logado (standard_user e performance_glitch_user)
Scenario Outline: Realizar login e validar que esta logado
When preencho o usuário '<usuario>' e senha '<senha>'
And avanço clicando no botão login
Then deve redirecionar para o catalogo de produtos

Examples:
  | usuario | senha |
  | standard_user | secret_sauce |
  | performance_glitch_user | secret_sauce |

#Realizar login e validar erro ao logar (locked_out_user)
Scenario: Realizar login e validar erro ao logar
When preencho o usuário locked_out_user e senha secret_sauce
And avanço clicando no botão login
Then deve exibir mensagem de usuário bloqueado

#Realizar login e em seguida realizar o logout (standard_user)
Scenario: Realizar login e em seguida realizar o logout
When realizo login com sucesso com o usuário standard_user e senha secret_sauce
And expando o menu lateral do site
And seleciono logout
Then deve ter realizado logout do sistema e voltar para a tela de login

#Realizar login, adicionar mais de um item no carrinho e então fazer
#_todo o processo para finalizar uma compra. (standard_user)
Scenario Outline: Formalizar compra
Given realizo login com sucesso com o usuário standard_user e senha secret_sauce
When coloco <quantidade> itens no carrinho
And clico em checkout
And preencho as informações
Then devem haver <quantidade> itens no checkout
Then deve exibir mensagem de compra concluida ao finalizar

Examples:
  |quantidade|
  |2         |
  |4         |
  |6         |

# Realizar login, filtrar os itens de mais caros a mais barato, adicionar os dois itens
# mais caros no carrinho e então fazer_todo o processo para finalizar uma compra. (standard_user)
Scenario: Formalizar compra - mais caros
Given realizo login com sucesso com o usuário standard_user e senha secret_sauce
When ordeno do mais caro ao mais barato
And coloco 2 itens no carrinho
And clico em checkout
And preencho as informações
Then devem haver 2 itens no checkout
And deve exibir mensagem de compra concluida ao finalizar


#Realizar login, adicionar um item no carrinho e validar erro ao tentar finalizar a compra. (problem_user)
Scenario: Erro ao finalizar compra
Given realizo login com sucesso com o usuário problem_user e senha secret_sauce
And coloco 1 itens no carrinho
And clico em checkout
And preencho as informações
Then o campo last name fica em branco
And é apresentada mensagem de last name sem preenchimento
