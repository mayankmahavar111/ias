import requests
import time
from bs4 import BeautifulSoup
from urllib import urlencode
from urllib import urlopen

# Get sitemap

sitemap_url = 'https://pythonmatplotlibtips.blogspot.com/sitemap.xml'
data = urlopen(sitemap_url).read()
data = str(data)
splited = data.replace("</loc>","<loc>").split("<loc>")
urls = [ url for url in splited if 'pythonmatplotlibtips.blogspot.com' in url]

# Check if the url has been indexed

seconds = 10

proxies = {
    'https' : 'https://localhost:8123',
    'http' : 'http://localhost:8123'
    }

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
headers = { 'User-Agent' : user_agent}

indexed = []
notindexed = []
retvals = []
for line in urls:
    query = {'q': 'info:' + line}
    google = "https://www.google.com/search?" + urlencode(query)
    data = requests.get(google, headers=headers)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")
    try:
        check = soup.find(id="rso").find("div").find("div").find("h3").find("a")["href"]
        indexed.append(line)
    except AttributeError:
        notindexed.append(line)
    time.sleep(float(seconds))


yind = "\n".join(indexed)
ny = len(indexed)
nind = "\n".join(notindexed)
nn = len(notindexed)
content1 = "URL of sitemap:\n%s"%(sitemap_url)
content2 = "There are %d indexed URLs:\n%s"%(ny,yind)
content3 = "There are %d NOT indexed URLs\n%s"%(nn,nind)
content  = "\n%s\n\n\n%s\n\n%s"%(content1,content2,content3)
print(content)