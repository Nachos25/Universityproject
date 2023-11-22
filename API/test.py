import bs4
import requests
from requests import Session
from fake_useragent import UserAgent

ua = UserAgent().random
headers = {"User-Agent": ua}
link = "https://jabko.ua/mac/imac/apple-imac-2023-/apple-imac-24-retina-45k-apple-m3-256gb-8-cpu-10-gpu-8gb-ram-purple-2023"

request = requests.get(url=link, headers=headers).text
print(bs4.BeautifulSoup(request, 'lxml').find_all('script'))

