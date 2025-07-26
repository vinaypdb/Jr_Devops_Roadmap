import requests

urls = ['https://google.com', 'https://github.com']
for url in urls:
    r = requests.get(url)
    print(f"{url} is {'UP' if r.status_code == 200 else 'DOWN'}")
