import requests
res = requests.get('http://127.0.0.1:8001/api/customers')
print(res.status_code)
# data = res.json()
#
# for item in data:
#     print("ID: ", item['id'])
#     print("Name: ", item['name'])
#     print("--------")
