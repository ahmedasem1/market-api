import requests

endpoint = "http://localhost:8000/api/products/0/" 

get_response = requests.get(endpoint) 
print(get_response)