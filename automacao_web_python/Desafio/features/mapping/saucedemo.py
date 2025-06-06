from selenium.webdriver.common.by import By
from common.base_page import BasePage
from main import debug

class Site (BasePage):

    __URL = "https://www.saucedemo.com/"

    __login_logo = (By.CLASS_NAME, "login_logo")
    __app_logo = (By.CLASS_NAME, "app_logo")

    __compra_concluida_msg = (By.CLASS_NAME, "complete-header")
    __block_msg = (By.XPATH, '''// *[ @ id = "login_button_container"] / div / form / div[3] / h3''')
    __last_name_err_msg = (By.XPATH, '''//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3''')

    __user_field = (By.ID, "user-name" )
    __password_field = (By.ID, "password")
    __first_name_field = (By.ID, "first-name")
    __last_name_field = (By.XPATH, '''//*[@id="last-name"]''')
    __zip_code_field = (By.ID, "postal-code")

    __login_btn = (By.XPATH, '''// *[ @ id = "login-button"]''')
    __logout_btn = (By.XPATH, '''// *[ @ id = "logout_sidebar_link"]''')
    __menu_btn = (By.XPATH, '''// *[ @ id = "react-burger-menu-btn"]''')
    __carrinho_btn = (By.XPATH, '''//*[@id="shopping_cart_container"]/a''')
    __checkout_btn = (By.XPATH, '''//*[@id="checkout"]''')
    __continue_btn = (By.XPATH, '''// *[ @ id = "continue"]''')
    __finish_btn = (By.XPATH, '''// *[ @ id = "finish"]''')

    __cart_list_div = (By.XPATH, '''// *[ @ id = "checkout_summary_container"] / div / div[1]''')

# Navegação

    def ir_para_saucedemo_login_page(self):
        if debug:
            print(f'DEBUG MODE -> saucedemo.py -> Navegando até {self.__URL}')

        self._go_to_url(Site.__URL)


# Ações

    def preencher_usuario_e_senha(self, usuario, senha):
        if debug:
            print(f'DEBUG MODE -> saucedemo.py -> Preenchendo usuário {usuario} e senha {senha} no formulário')

        self._send_keys(self.__user_field, usuario)
        self._send_keys(self.__password_field, senha)


    def clicar_no_botao_login(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> Clicando no botão "Login"')

        self._wait_and_click_element(self.__login_btn)


    def clicar_no_botao_logout(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> Clicando no botão "Logout"')

        self._wait_and_click_element(self.__logout_btn)


    def clicar_no_menu_lateral(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> Clicando no menu lateral')

        self._wait_and_click_element(self.__menu_btn)

    def adicionar_itens_ao_carrinho(self, quantidade: int):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> Adicionando itens...')

        for item in range(quantidade):
            if debug:
                print(f'DEBUG MDOE -> saucedemo.py -> for item -> item {item+1}')
            __add_to_cart_btn = (By.XPATH, f'''/ html / body / div / div / div / div[2] / div / div / div / div[{item+1}] / div[2] / div[2] / button''')

            if debug:
                print(f'DEBUG MDOE -> saucedemo.py -> for item -> locator do item: {__add_to_cart_btn}')
            self._wait_and_click_element(__add_to_cart_btn)

    def confirmar_compra(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> click carrinho')
        self._wait_and_click_element(self.__carrinho_btn)
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> click checkout')
        self._wait_and_click_element(self.__checkout_btn)


    def preencher_informacoes(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> preenchendo campos')
        self._send_keys(self.__first_name_field, "nome")
        self._send_keys(self.__last_name_field, "sobrenome")
        self._send_keys(self.__zip_code_field, "123456")
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> click continuar')
        self._wait_and_click_element(self.__continue_btn)

    def finalizar_compra(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> click finish')
        self._wait_and_click_element(self.__finish_btn)


    def ordernar_catalogo(self, metodo:str):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> metodo de ordenação selecionado: {metodo}')

        if metodo != 'az' and metodo != 'za' and metodo != 'hilo' and metodo != 'lohi':
            print(f'DEBUG MDOE -> saucedemo.py -> metodo de ordenação {metodo} inválido! Selecionado: "az"')
            metodo = 'az'

        __sort_dropdown = (By.XPATH, f'''//*[@id="header_container"] //select /option[@value="{metodo}"]''')
        self._click_element(__sort_dropdown)

    #Validações

    def usuario_esta_na_login_page(self) -> bool:
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se está na tela de login')

        return self._is_element_present(self.__login_logo)

    def usuario_esta_na_home(self) -> bool:
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se está na home')

        return self._is_element_present(self.__app_logo)

    def usuario_esta_bloqueado(self) -> bool:
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se usuário está bloqueado')
        return self._is_element_present(self.__block_msg)

    def validar_compra_concluida(self) -> bool:
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se a compra foi concluida')
        return self._is_element_present(self.__compra_concluida_msg)

    def validar_itens_no_checkout(self, quantidade: int) -> bool:
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se há {quantidade} itens no checkout')
        div = self._returns_element(self.__cart_list_div)
        itens = div.find_elements(By.CLASS_NAME, "cart_item")
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> Há {len(itens)} itens no checkout')

        return quantidade == len(itens)


    def validar_preenchimento_last_name(self, comp:int) -> bool:
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se last name foi preenchido')

        valor_atributo = self._returns_element(self.__last_name_field).get_attribute("value")
        print (f'Encontrou o campo preenchido com "{valor_atributo}"')

        if comp <= 0:
            return len(valor_atributo) == comp
        return len(valor_atributo) >= comp


    def validar_mensagem_erro_last_name(self):
        if debug:
            print(f'DEBUG MDOE -> saucedemo.py -> verificando se mensagem "Last Name is required" está presente')
        return self._is_element_present(self.__last_name_err_msg)
