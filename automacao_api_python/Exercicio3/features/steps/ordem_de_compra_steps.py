from behave import *
from features.impl.ordem_de_compra import OrdemDeCompra


@given(u'que o usuário selecionou o animal com o id correspondente a "{id}" desejado na petstore')
def step_impl(context, id):
    context.api = OrdemDeCompra()
    context.api.id = id
    context.api.petId = 2
    context.api.quantidade = 10
    context.api.post_criar_uma_nova_ordem()



@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context)  :
    pass



@given(u'que o usuário selecionou o id correspondente a "{id}" para remoção da ordem')
def step_impl(context, id):
    pass

@given(u'incluiu nova ordem "{id_nova_ordem}" para o animal selecionado na petstore')
def step_impl(context,id_nova_ordem):
    pass

@then(u'o sistema valida se a ordem foi removida com sucesso para a "{id}"')
def step_impl(context, id):
    pass

@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente com "{id_nova_ordem}"')
def step_impl(context, id_nova_ordem):
    pass