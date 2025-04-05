import requests

url = "http://example.com"

response = requests.get(url)

cookies = response.cookies

for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")
