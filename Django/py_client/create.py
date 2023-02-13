import requests

endpoint = "http://localhost:8000/api/blogs/posts"

# data = {'author': 1,
#         'title': 'sadasd',
#         'description': 'sadsad', 
#         'summary': 'sadsad',
#         'viewCount': 1,
#         'category': []
#         }
data = {
    'author': 1,
    'title': 'this ios aiosfks',
    'description': 'This is post description',
    'summary': 'This is post Summary',
    'views_count': 1,
    'category': []
}

get_response = requests.post(endpoint, json=data)
print(get_response.reason)
# print(get_response)
print(get_response.status_code)
# print(get_response.json())
