from requests import Response
from usuario import Usuario


class TestDesafio1:

    URL_NEW_USER = "https://petstore.swagger.io/v2/user"

    DATA = {
        "id": 0,
        "username": "gabriel",
        "firstName": "gabriel",
        "lastName": "rache",
        "email": "a123@a.a",
        "password": "password",
        "phone": "555199999999",
        "userStatus": 1
    }

    def test_validar_se_requisicao_post_retornou_200():

        response = Usuario.criar_usuario(URL_NEW_USER, DATA)
        assert response.status_code == 200