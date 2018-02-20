"""import requests
from bs4 import BeautifulSoup
r = requests.get("https://elearning.didacte.com/en/users/sign_up")
soup = BeautifulSoup(r.content,"html.parser")

src = [sc["src"] for sc in  soup.select("script[src]")]
print src"""
from bs4 import BeautifulSoup

import urllib
url="http://www.facebook.com"
page = urllib.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
icon_link = soup.find("link", rel="shortcut icon")
icon = urllib.urlopen(icon_link['href'])
with open("test.ico", "wb") as f:
    f.write(icon.read())
