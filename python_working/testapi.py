import requests # type: ignore
import json
api_key = '3805f6bbabcb42b3a0c08a489baf603d'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"
response = requests.get(url)
print(response.status_code)         # Api response 200 successfull

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
if response.status_code == 200:
    print(response.json())           #GET request is used to fetch data from an API
else:
    print("Error:", response.status_code)

url = "https://jsonplaceholder.typicode.com/posts"        #POST request is used to send data to the API
data = {
    "title": "New Post Created",
    "body": "In this New Post included the api post requests",
    "id": 2,
    "userId": 2
}
response = requests.post(url, json=data)      #send post request with json data
# print response
if response.status_code == 201:
    print(response.json())     # show created post details
else:
    print("Error:", response.status_code)      

url = "https://jsonplaceholder.typicode.com/posts/1"        #PUT request is used to update existing data
updated_data = {
    "tile": "New Post Updated",
    "body": "In this new post updated the api requests",
    "userId": 11
}
response = requests.put(url, json=updated_data)       # send put request
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)

url = "https://jsonplaceholder.typicode.com/posts/1"       #DELETE request is used to remove data
response = requests.delete(url)                            # send delete request
if response.status_code == 200:
    print("New post deleted successfully")
else:
    print("Error:", response.status_code)