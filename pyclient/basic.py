import requests
endpoint="http://localhost:8000/api/"

# endpoint="https://httpbin.org/anything"#anything (JSON)(REST)

get_response=requests.get(endpoint,params={"abc":123},json=

{"query":"hello"})#http request
print(get_response.status_code)#print text response code
print(get_response.text)#print text response code
print(get_response.json)#print text response code
