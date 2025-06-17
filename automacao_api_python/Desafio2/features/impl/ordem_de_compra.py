import requests
from datetime import datetime

class OrdemDeCompra:
    def __init__(self):
        self.url_petstore_order = 'https://petstore.swagger.io/v2/store/order'
        self.id = None
        self.petId = None
        self.quantidade = None
        self.data = datetime.now().isoformat()
        self.status_code = None

    def post_criar_uma_nova_ordem(self):
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        data = {
        "id": self.id,
        "petId": self.petId,
        "quantity": self.quantidade,
        "shipDate":  self.data,
        "status": "placed",
        "complete": True
        }
        response = requests.post(self.url_petstore_order, headers=header, json=data)
        self.status_code = response.status_code
        return response
    
    
    def get_validar_ordem_criada(self) -> bool:
        url_petstore_get = self.url_petstore_order + f"/{self.id}"
        response = requests.get(url_petstore_get)
        
        if response.json()["petId"] != 2:
            return False
        if response.json()['quantity'] != 10:
            return False
        return True
