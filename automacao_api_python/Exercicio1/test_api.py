import requests


class TestApiRestful:
    def test_get_object(self):
        url = "https://api.restful-api.dev/objects"
        id = 1
        params = {'id': id}
        response = requests.get(url, params=params)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data[0]['id'] == str(id)