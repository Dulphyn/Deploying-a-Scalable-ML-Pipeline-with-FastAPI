import json

import requests

url = "http://127.0.0.1:8000"
r = requests.get(url) # Your code here

get_status=r.status_code
print(f"Status Code: {get_status}")
get_response = r.json()["message"]
print(f"Result: {get_response}")

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

url_post = f"{url}/data/"
r = requests.post(url_post, data = json.dumps(data)) # Your code here

post_status=r.status_code
print(f"Status Code: {post_status}")

post_response = r.json()["result"]
print(f"Result: {post_response}")
