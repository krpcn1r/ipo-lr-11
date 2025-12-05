from bs4 import BeautifulSoup as bs
import requests 
import json

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

data_dict = dict(zip(data_countries, data_capitals))

for i in range(len(data_countries)):
    print(f"{i + 1}. Country: {list(data_dict.keys())[i]}; Capital: {list(data_dict.values())[i]};")


with open("C:/Users/ZaytsSte_89/Documents/Visual Studio 2022/Python/data.json", "w", encoding = "utf-8") as file:
    json.dump(data_dict, file, ensure_ascii=False, indent=4)
    print("Данные записаны")

with open("C:/Users/ZaytsSte_89/Documents/Visual Studio 2022/Python/data.json", "r", encoding = "utf-8") as file:
    load_data = json.load(file)
    info = json.dumps(load_data, ensure_ascii=False)

    info_keys = load_data.keys()
    info_values = load_data.values()

    rows = ""

    for a,b in zip(info_keys, info_values):
        row = f"""
        <tr>
            <td>
                {a}
            </td>
            <td>
                {b}
            </td>
        </tr>
        """
        rows += row
    
    html = f"""
            <html>
                <head>
                    <title>
                        Список стран
                    </title>
                </head>
                <body style="background-color: #f0f0ff;">
                    <h1 align="center">
                        Список стран
                    </h1>
                    <table width = "50%", border="1", cellpadding="4", cellspacing="0", align="center">
                        <tr>
                        <th>
                            Страны
                        </th> 
                        <th>
                            Столицы
                        </th> 
                        </tr>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </body>
            </html>
            """

with open("C:/Users/ZaytsSte_89/Documents/Visual Studio 2022/Python/output.html", "w", encoding="utf-8") as file:
    file.write(html)
