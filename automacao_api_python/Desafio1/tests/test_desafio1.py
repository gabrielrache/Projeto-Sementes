import requests
from pytest import fixture

URL_NEW_USER = "https://petstore.swagger.io/v2/user"
URL_USER = f"https://petstore.swagger.io/v2/user/grc"

DATA_NEW_USER = {
    "id": 0,
    "username": "grc",
    "firstName": "gabriel",
    "lastName": "carmona",
    "email": "gabriel.carmona@domain.com",
    "password": "123",
    "phone": "987654321",
    "userStatus": 0
}

DATA_UPDATE_USER = {
    "id": 0,
    "username": "grc",
    "firstName": "gabriel",
    "lastName": "carmona",
    "email": "gabriel@domain.com",
    "password": "123",
    "phone": "987654321",
    "userStatus": 0
}

HEADER_CONTENT_TYPE = {'Content-Type': 'application/json'}


@fixture
def novo_usuario():
    response = requests.post(url = URL_NEW_USER, json = DATA_NEW_USER)
    return response



def test_validar_se_requisicao_post_retornou_ok(novo_usuario):
    assert novo_usuario.status_code == 200
    
    json_data = novo_usuario.json()
    assert json_data['type'] == "unknown"
    
    
    
def test_validar_se_requisicao_get_retornou_ok(novo_usuario):
    response = requests.get(url = URL_USER)
    assert response.status_code == 200
    
    json_data = response.json()
    assert json_data['firstName'] == "gabriel"


def test_validar_se_requisicao_put_retornou_ok(novo_usuario):
    response = requests.put(url = URL_USER, json =DATA_UPDATE_USER)
    assert response.status_code == 200
    
    json_data = response.json()
    
    print (json_data)
    assert json_data['type'] == "unknown"    


def test_validar_se_requisicao_delete_retornou_ok(novo_usuario):
    response = requests.delete(url = URL_USER, json =DATA_UPDATE_USER)
    assert response.status_code == 200
    
    json_data = response.json()
    
    print (json_data)
    assert json_data['message'] == "grc"

