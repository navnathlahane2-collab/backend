import requests
from bs4 import BeautifulSoup

def get_flipkart_price(product):
    try:
        url = f"https://www.flipkart.com/search?q={product.replace(' ', '%20')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find("div", class_="_30jeq3")
        return int(price.text.replace("₹","").replace(",","")) if price else None
    except:
        return None
