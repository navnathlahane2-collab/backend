from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper.amazon import get_amazon_price
from scraper.flipkart import get_flipkart_price
from ml.price_compare import compare_prices
from database.db_manager import save_price, fetch_history

app = FastAPI(title="Smart Deal Finder API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/ping")
def ping():
    return {"status": "API running"}

@app.get("/search")
def search(product: str):
    amazon = get_amazon_price(product)
    flipkart = get_flipkart_price(product)
    prices = {"Amazon": amazon, "Flipkart": flipkart}
    save_price(product, prices)
    return {
        "prices": prices,
        "best_deal": compare_prices(prices)
    }

@app.get("/history")
def history(product: str):
    data = fetch_history(product)
    return {"history": data}
