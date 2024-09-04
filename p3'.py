class Portfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            print(f"{symbol} not found in the portfolio!")

    def get_stock_price(self, symbol):
        # Simulated stock prices (hardcoded data)
        simulated_prices = {
            "AAPL": 150.00,
            "GOOGL": 2800.00,
            "MSFT": 300.00,
            "AMZN": 3500.00
        }
        return simulated_prices.get(symbol.upper(), None)

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
    tracker = Portfolio()

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
