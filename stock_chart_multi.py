import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_multiple_stocks(tickers, years):
    # Calculate start and end dates
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years*365)

    plt.figure(figsize=(14,7))

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)

        if data.empty:
            print(f"No data found for {ticker}")
            continue

        plt.plot(data.index, data['Close'], label=ticker)

    plt.title(f"Stock Price Comparison for Last {years} Years")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.legend()
    plt.show()

# --- Main ---
if __name__ == "__main__":
    tickers_input = input("Enter stock tickers separated by comma (e.g., AAPL,VOO,MSFT): ")
    tickers = [t.strip().upper() for t in tickers_input.split(",")]

    while True:
        try:
            years = int(input("Enter number of years to compare: "))
            break
        except ValueError:
            print("Please enter a valid number of years!")

    plot_multiple_stocks(tickers, years)
