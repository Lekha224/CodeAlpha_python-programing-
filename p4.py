
class Portfolio:
    def __init__(self, api_key):
        self.portfolio = {}
        self.api_key = api_key

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            print(f"{symbol} not found in the portfolio!")

    def fetch_data(self, symbol):
        endpoint = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "5min",
            "apikey": self.api_key
        }
        response = requests.get(endpoint, params=params)
        return response.json()

    def get_stock_price(self, symbol):
        data = self.fetch_data(symbol)
        if 'Time Series (5min)' in data:
            latest_time = list(data['Time Series (5min)'].keys())[0]
            return float(data['Time Series (5min)'][latest_time]['4. close'])
        else:
            print(f"Error fetching data for {symbol}.")
            return None

    def display_portfolio(self):
        print("\nCurrent Portfolio:")
        for symbol, shares in self.portfolio.items():
            stock_price = self.get_stock_price(symbol)
            if stock_price:
                total_value = stock_price * shares
                print(f"{symbol}: {shares} shares at ${stock_price:.2f} each, Total Value: ${total_value:.2f}")
            else:
                print(f"{symbol}: {shares} shares (Price unavailable)")
        print("---------------------------------------------------------")

if __name__ == "__main__":
    api_key = input("Enter your Alpha Vantage API key: ")
    tracker = Portfolio(api_key)

    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            tracker.remove_stock(symbol)
        elif choice == "3":
            tracker.display_portfolio()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
  
