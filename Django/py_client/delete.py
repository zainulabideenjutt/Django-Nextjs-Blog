import requests

endpoint = "http://localhost:8000/api/blogs/posts/8/delete" 

get_response = requests.delete(endpoint) 
print(get_response.status_code)