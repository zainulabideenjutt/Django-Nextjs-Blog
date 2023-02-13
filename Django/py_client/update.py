import requests

endpoint = "http://localhost:8000/api/blogs/1/update" 

data = {
    "title": "Updated title",
    "description": "Updated description",
    "summary": "Updated Summary",
}
get_response = requests.put(endpoint, json=data) 
print(get_response.json())