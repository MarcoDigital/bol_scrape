import requests
from bs4 import BeautifulSoup
import time
import webbrowser
import sys

url = "https://www.bol.com/nl/p/apple-airpods-pro-met-active-noise-cancelling/9200000123229147/"  # Bol.com link
targetprijs = float(10.15)  # Voer hier je targetprijs in. Voorbeeld: 24.53
interval = 15  # Getal in seconde


def bolchecker():
    request = requests.get(url).text
    soup = BeautifulSoup(request, 'html.parser')
    try:
        prijs = soup.find(class_="promo-price").get_text()
        prijs1 = int(prijs[0:3])
        try:
            prijs2 = int(prijs[-4:-1])
        except:
            prijs2 = int(00)
        prijs3 = float(str(prijs1) + "." + str(prijs2))
        return prijs3
    except:
        pass


prijsproduct = bolchecker()


def prijschecker(prijsproduct, targetprijs):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    try:
        if targetprijs > prijsproduct:
            print(
                f"\nHet product is afgekort. Het kost nu €{prijsproduct}. Jouw targetprijs is €{targetprijs}. De tijd is: {current_time}.\nHier is de link: {url}. ")
            sendmail()
        elif targetprijs < prijsproduct:
            print(
                f"Het product is NIET afgekort. Het kost €{prijsproduct}. Jouw targetprijs is €{targetprijs}. De tijd is: {current_time} ")
            return False
    except TypeError:
        print(f"Het product is momenteel uit voorraad. Tijd: {current_time}")


def sendmail():
    print("Opent URL...")
    webbrowser.open(url)
    print("Stopt programma\n")
    sys.exit()


while True:
    prijschecker(prijsproduct, targetprijs)
    time.sleep(interval)
