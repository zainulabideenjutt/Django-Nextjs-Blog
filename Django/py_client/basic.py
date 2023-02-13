import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/blogs/"

get_response = requests.get(endpoint,
                            # data={'message':"this is the data message"},
                            # json={'message':"this is the Json"},
                            params={'message':"this is the params message"},headers={'Content-Type': 'application/json'}) # HTTP Request
# print(get_response.text) # print raw text response


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
print(get_response.headers)
print(get_response.json())
# print(get_response.status_code)
