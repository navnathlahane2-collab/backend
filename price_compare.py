def compare_prices(prices):
    valid = {k:v for k,v in prices.items() if v is not None}
    return min(valid, key=valid.get) if valid else "No price found"
