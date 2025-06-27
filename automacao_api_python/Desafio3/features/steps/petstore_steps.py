from behave import given, when, then
from features.impl.petstore import Petstore

@given(u'que estou usando a api da petstore')
def step_impl(context):
    context.api = Petstore()

@given(u'que tenho uma lista de usuários')
def step_impl(context):
    context.lista = context.api.criar_lista_de_usuarios(3)

@when(u'cadastro os usuários através da opção de lista')
def step_impl(context):
    context.response = context.api.post_lista_de_usuarios(context.lista)

@then(u'haverá retorno 200')
def step_impl(context):
    assert context.response.status_code == 200

@then(u'haverá mensagem "{mensagem}" no corpo')
def step_impl(context, mensagem):
    assert context.api.validar_mensagem_recebida(context.response, mensagem)

##

@given(u'que tenho um usuário cadastrado')
def step_impl(context):
    context.lista = context.api.criar_lista_de_usuarios(1)
    context.response = context.api.post_lista_de_usuarios(context.lista)

@when(u'buscar as informações do usuario')
def step_impl(context):
    context.response = context.api.get_informacoes_do_usuario(context.lista[0])

@then(u'os dados retornarão no corpo')
def step_impl(context):
    assert context.api.validar_dados_do_usuario(context.response, context.lista[0])

##

@given (u'tenho as novas informações para atualizar')
def step_impl(context):
    context.informacoes = context.api.criar_lista_de_usuarios(1)

@when(u'atualizo as informações')
def step_impl(context):
    context.response = context.api.put_informacoes_do_usuario(context.lista[0], context.informacoes[0])

##

@when(u'removo o usuário')
def step_impl(context):
    context.response = context.api.delete_usuario(context.lista[0])

