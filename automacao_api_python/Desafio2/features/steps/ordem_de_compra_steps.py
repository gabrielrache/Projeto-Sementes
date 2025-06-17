from behave import given, then

from features.impl.ordem_de_compra import OrdemDeCompra
     

@given(u'que o usuário selecionou o animal desejado na petstore')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.id = 4
    context.api.petId = 2
    context.api.quantidade = 10
    context.api.post_criar_uma_nova_ordem()



@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    assert context.api.get_validar_ordem_criada()
     