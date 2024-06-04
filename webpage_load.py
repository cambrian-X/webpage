import requests
from browser import headers

link= input("Enter link address: ")
source=requests.get(link,headers=headers).text
with open('webpage.html', "w", encoding="utf-8") as f:
    f.write(source)
f.close()
