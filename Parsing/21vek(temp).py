import requests
from bs4 import BeautifulSoup
a=set()
r=requests.get("https://www.21vek.by/")
soup = BeautifulSoup(r.text,'lxml')
soup = soup.findAll('span',class_="styles-moduleQc4Xjg5U9Q")
for i in soup:
    a.add(i.get_text())

for j in sorted(a):
    print(j)
print("GIT")
print("KOLIA")
print("Добавил на компике,проверка десктоп приложения")



