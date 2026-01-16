import requests
from bs4 import BeautifulSoup

def get_amazon_price(product):
    try:
        url = f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find("span", class_="a-price-whole")
        return int(price.text.replace(",", "")) if price else None
    except:
        return None
