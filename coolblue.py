from bs4 import BeautifulSoup
import requests

url = "https://www.coolblue.nl/product/829696/gear4-oxford-huawei-p30-book-case-zwart.html"

request = requests.get(url).text
soup = BeautifulSoup(request, "html.parser")


def coolblue_price():
    for i, prijs in enumerate(soup.find_all(class_="sales-price__current")):
        if i == 0:
            nummer = prijs.getText()
            try:
                x = nummer.replace(",-", "")
                final = float(x)
                return final
            except ValueError:
                comma = nummer.replace(",", ".")
                final = float(comma)
                return final


print(coolblue_price())
