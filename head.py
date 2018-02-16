import requests as req

resp = req.get("http://google.com", allow_redirects=False)

print(resp.status_code)
print(resp.url)