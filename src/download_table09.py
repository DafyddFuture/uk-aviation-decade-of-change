import requests

url = "https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/uk-airport-data-2015/january-2015/"

response = requests.get(url)

from bs4 import BeautifulSoup
from urllib.parse import urljoin

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a")

for link in links:
    if "Table 09" in link.get_text() and "CSV" in link.get_text():
        print(link.get_text(strip=True))
        csv_url = urljoin(url, link.get("href"))
        print(csv_url)
        csv_response = requests.get(csv_url)
        print(csv_response.status_code)

        file_path = "data/raw/table09_2015_01.csv"

with open(file_path, "wb") as file:
    file.write(csv_response.content)

print(response.status_code)
print(len(links))
