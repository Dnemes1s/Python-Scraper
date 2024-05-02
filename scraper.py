import requests 
from bs4 import BeautifulSoup  

page_to_scrape = requests.get("https://data.sa.gov.au/data/dataset/popular-baby-names/resource/b5215a01-36b6-4765-92fb-87296fb48042")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
names = soup.findALL("div", attrs={"Class":"HENRY"})

for name in names:
    print(name.text)
