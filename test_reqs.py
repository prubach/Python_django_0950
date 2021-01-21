import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/customers/'

#response = requests.get(url, auth=HTTPBasicAuth('admin', '123'))
response = requests.get(url)

json_data = response.json()
print(json_data)
print(json_data[0]['email'])

newcust = {
    "first_name": "Pawel",
    "last_name": "Rubach",
    "email": "pawel@smith.com",
    "birth_date": "2020-11-03"
}

#response = requests.post(url, data=newcust, auth=HTTPBasicAuth('admin', '123'))
response = requests.post(url, data=newcust)
print(response.json())
