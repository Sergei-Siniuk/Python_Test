import requests
import json
from bs4 import BeautifulSoup

url = "http://www.ecopress.by/ru/page/60.html"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text

with open("index.html", "w", encoding="utf-8-sig") as file:
    file.write(src)
print(src)
