import requests
# response = requests.get("http://api.open-notify.org/astros.json")
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
response = requests.get("http://azr.ir/api/posts/10")
print(response.json())