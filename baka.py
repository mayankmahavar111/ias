from bs4 import BeautifulSoup

import urllib
url="http://www.youtube.com"
page = urllib.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
icon_link = soup.find("link", rel="shortcut icon")
icon = urllib.urlopen(icon_link['href'])
print (icon_link['href'])
with open("test.ico", "wb") as f:
    f.write(icon.read())
