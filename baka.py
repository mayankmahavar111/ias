import requests
from bs4 import BeautifulSoup
r = requests.get("https://elearning.didacte.com/en/users/sign_up")
soup = BeautifulSoup(r.content,"html.parser")

src = [sc["src"] for sc in  soup.select("script[src]")]
print src