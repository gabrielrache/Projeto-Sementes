from behave import given, when, then, step
from features.mapping.saucedemo import Site


@given("que acesso o site saucedemo")
def step_impl(context):
    context.saucedemo_page = Site()
    context.saucedemo_page.ir_para_saucedemo_login_page()


@given("realizo login com sucesso com o usuário problem_user e senha secret_sauce")
def step_impl(context):
    context.saucedemo_page.preencher_usuario_e_senha('problem_user', 'secret_sauce')
    context.saucedemo_page.clicar_no_botao_login()


@when("preencho o usuário '{usuario}' e senha '{senha}'")
def step_impl(context, usuario, senha):
    context.saucedemo_page.preencher_usuario_e_senha(usuario, senha)


@when("preencho o usuário locked_out_user e senha secret_sauce")
def step_impl(context):
    context.saucedemo_page.preencher_usuario_e_senha('locked_out_user', 'secret_sauce')


@when("avanço clicando no botão login")
def step_impl(context):
    context.saucedemo_page.clicar_no_botao_login()


@when("ordeno do mais caro ao mais barato")
def step_impl(context):
    context.saucedemo_page.ordernar_catalogo("hilo")


@step("realizo login com sucesso com o usuário standard_user e senha secret_sauce")
def step_impl(context):
    context.saucedemo_page.preencher_usuario_e_senha('standard_user', 'secret_sauce')
    context.saucedemo_page.clicar_no_botao_login()


@step("seleciono logout")
def step_impl(context):
    context.saucedemo_page.clicar_no_botao_logout()


@step("expando o menu lateral do site")
def step_impl(context):
    context.saucedemo_page.clicar_no_menu_lateral()


@step("coloco {quantidade} itens no carrinho")
def step_impl(context, quantidade: int):
    context.saucedemo_page.adicionar_itens_ao_carrinho(int(quantidade))


@step("clico em checkout")
def step_impl(context):
    context.saucedemo_page.confirmar_compra()


@step("preencho as informações")
def step_impl(context):
    context.saucedemo_page.preencher_informacoes()


@step("devem ser os produtos mais caros")
def step_impl(context):
    assert context.saucedemo_page.validar_produtos_mais_caros()


@then("deve redirecionar para o catalogo de produtos")
def step_impl(context):
    assert context.saucedemo_page.usuario_esta_na_home()


@then("deve exibir mensagem de usuário bloqueado")
def step_impl(context):
    assert context.saucedemo_page.usuario_esta_bloqueado()


@then("deve ter realizado logout do sistema e voltar para a tela de login")
def step_impl(context):
    assert context.saucedemo_page.usuario_esta_na_login_page()


@then("deve exibir mensagem de compra concluida ao finalizar")
def step_impl(context):
    context.saucedemo_page.finalizar_compra()
    assert context.saucedemo_page.validar_compra_concluida()


@then("devem haver {quantidade} itens no checkout")
def step_impl(context, quantidade: int):
    assert context.saucedemo_page.validar_itens_no_checkout(int(quantidade))


@then("é apresentada mensagem de last name sem preenchimento")
def step_impl(context):
    assert context.saucedemo_page.validar_mensagem_erro_last_name()


@then("o campo last name fica em branco")
def step_impl(context):
    assert context.saucedemo_page.validar_preenchimento_last_name(0)