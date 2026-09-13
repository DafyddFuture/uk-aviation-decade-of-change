import calendar
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


for year in range(2015, 2026):

    for month in range(1, 13):
            month_name = calendar.month_name[month].lower()

            url = f"https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/uk-airport-data-{year}/{month_name}-{year}/"

            response = requests.get(url)


            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")

            for link in links:
                if "Table 09" in link.get_text() and "CSV" in link.get_text():
                    print(link.get_text(strip=True))
                    csv_url = urljoin(url, link.get("href"))
                    print(csv_url)
                    csv_response = requests.get(csv_url)
                    print(csv_response.status_code)

                    file_path = f"data/raw/table09_{year}_{month:02d}.csv"

                    with open(file_path, "wb") as file:
                        file.write(csv_response.content)

            print(response.status_code)
            print(len(links))
