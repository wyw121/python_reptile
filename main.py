
import requests

def get_binance_symbols():
    binance_url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(binance_url)
    data = response.json()
    symbols = [symbol['symbol'] for symbol in data['symbols']]
    return symbols

def get_okx_symbols():
    okx_url = "https://www.okx.com/api/v5/market/tickers?instType=SPOT"
    response = requests.get(okx_url)
    data = response.json()
    symbols = [ticker['instId'] for ticker in data['data']]
    return symbols

def main():
    binance_symbols = get_binance_symbols()
    print("Binance Symbols:", binance_symbols)
    
    okx_symbols = get_okx_symbols()
    print("OKX Symbols:", okx_symbols)

# 注释
if __name__ == "__main__":
    main()
