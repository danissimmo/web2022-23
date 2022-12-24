import requests
from pprint import pprint
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, type(r.text), r.json())
# r = requests.post('http://127.0.0.1:5000/users', json={
#     "id": 2,
#     "name": "Daniil",
#     "surname": "Medvedev"
#     })
# pprint(r.json())

# r = requests.post('http://127.0.0.1:5000/users', json={
#     "user_name": "Robert",
#     "user_surname": "Broke"
#     })
# r = requests.post('http://127.0.0.1:5000/users', json={
#     "user_name": "Blue",
#     "user_surname": "Red"
#     })
# pprint(r.json())

# r = requests.put('http://127.0.0.1:5000/users', json={
#     "user_id": 19,
#     "user_name": "Robert",
#     "user_surname": "Chkalov"
#     })
# pprint(r.json())
r = requests.delete('http://127.0.0.1:5000/users', json={
    "user_id": 19,
    })
# pprint(r.text)