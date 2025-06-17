import requests
from requests import Response


class Usuario:

    def criar_usuario(self, url: str, data: dict) -> Response:
        response = requests.post(url, json=data)
        print(response.json())

        return response
