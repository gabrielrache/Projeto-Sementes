import time

import requests
from features.impl.usuario import Usuario


class Petstore:

    def __init__(self):
        self.BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
        self.ENDPOINT_USER_BASE = '/user'
        self.ENDPOINT_USER_CREATE = '/user/createWithList'

    def criar_lista_de_usuarios(self, quantidade) -> list:
        lista = []

        for i in range(quantidade):
            lista.append(Usuario().__dict__)
            print (f"DEBUG: Usuário {lista[i]["username"]} adicionado à lista" )
        return lista

    def post_lista_de_usuarios(self, lista: list) -> requests.Response:
        url = self.BASE_URL_PETSTORE + self.ENDPOINT_USER_CREATE

        header_post = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        data = lista
        print(f"DEBUG: Lista de usuários enviada: {data}")

        response = requests.post(url, headers=header_post, json=data)
        print(f"DEBUG: Response recebido: {response.text}")
        return response

    def get_informacoes_do_usuario(self, usuario) -> requests.Response:
        username = usuario["username"]
        url = self.BASE_URL_PETSTORE + self.ENDPOINT_USER_BASE + '/' + username
        print(f"DEBUG: URL acessada: {url}")

        header_get = {
            'Accept': 'application/json',
        }

        response = None

        for tentativa in range(1, 4):

            response = requests.get(url, headers=header_get)
            if response.status_code == 200:
                break
            else:
                print(f"DEBUG: Tentativa de GET nº{tentativa} "
                      f"falhou com status {response.status_code}")

                if tentativa < 4:
                    print(f"DEBUG: Aguardando 2 segundos antes de tentar novamente...")
                    time.sleep(2)
        print(f"DEBUG: Response recebido: {response.text}")
        return response

    def validar_dados_do_usuario(self, response: requests.Response, usuario: dict) -> bool:
        print(F"DEBUG: Usuário enviado: {usuario['username']}")
        print(F"DEBUG: Response recebido: {response.json()}")

        validacao = response.json()["username"] == usuario["username"] and response.json()["email"] == usuario["email"]
        print(f"DEBUG: Validação = {validacao}")

        return validacao

    def put_informacoes_do_usuario(self, usuario: dict, informacoes: dict) -> requests.Response:
        username = usuario["username"]
        url = self.BASE_URL_PETSTORE + self.ENDPOINT_USER_BASE + '/' + username
        print(f"DEBUG: URL acessada: {url}")

        header_put = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'api_key': 'special-key'
        }

        response = None

        for tentativa in range(1, 4):
            response = requests.put(url, headers=header_put, json=informacoes)
            print(f"DEBUG: Response recebido: {response.text}")

            if response.status_code == 200:
                break
            else:
                print(f"DEBUG: Tentativa de PUT nº{tentativa} "
                      f"falhou com status {response.status_code}")

                if tentativa < 4:
                    print(f"DEBUG: Aguardando 2 segundos antes de tentar novamente...")
                    time.sleep(2)
        return response

    def delete_usuario(self, usuario: dict) -> requests.Response:
        username = usuario["username"]
        url = self.BASE_URL_PETSTORE + self.ENDPOINT_USER_BASE + '/' + username
        print(f"DEBUG: URL acessada: {url}")


        for tentativa in range(1, 5):
            response = requests.delete(url)
            print(f"DEBUG: Response recebido: {response.text}")

            if response.status_code == 200:
                break
            else:
                print(f"DEBUG: Tentativa de DELETE nº{tentativa} "
                      f"falhou com status {response.status_code}")

                if tentativa < 5:
                    print(f"DEBUG: Aguardando 3 segundos antes de tentar novamente...")
                    time.sleep(3)
        return response

    def validar_mensagem_recebida(self, response: requests.Response, mensagem: str) -> bool:
        print(f"DEBUG: Body recebido{response.json()}")
        print(f"DEBUG: mensagem procurada: {mensagem}")

        validacao = response.json()["message"] == mensagem
        print(f"DEBUG: validação: {validacao}")
        return validacao
