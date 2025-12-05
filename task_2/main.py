from bs4 import BeautifulSoup as bs
import requests 

URL = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(URL)
response.raise_for_status()

soup = bs(response.text, 'html.parser')
countries = soup.find_all('div', class_='country')
capitals = soup.find_all("div", class_ = "country-info")

data_countries = []
data_capitals = []

for i in countries:
    data_countries.append(i.find("h3", class_= "country-name").text.strip())

for i in capitals:
    data_capitals.append(i.find("span", class_ = "country-capital").text.strip())

for i in range(len(data_countries)):
    print(f"{i + 1}. Country: {data_countries[i]}; Capital: {data_capitals[i]};")
