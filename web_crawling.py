import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    for link in soup.find_all("a"):
        print(link.get("href"))
else:
    print("Failed to retrieve the web page")
