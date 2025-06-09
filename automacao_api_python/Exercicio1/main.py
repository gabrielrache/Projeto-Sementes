import requests

url = "https://api.restful-api.dev/objects"

response = requests.get(url=url)
print(response.json())

#############################

data = {'id':1}
response = requests.get(url=url,data=data)

assert response.status_code == 200

json_data = response.json()
assert json_data[0]['id'] == '1'
print(json_data[0])

#############################