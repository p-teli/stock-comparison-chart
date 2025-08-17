import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_percentage_change(tickers, years):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years*365)

    plt.figure(figsize=(14,7))
    
    total_changes = {}  # Store total percentage change for each stock

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)

        if data.empty:
            print(f"No data found for {ticker}")
            continue

        # Calculate percentage change relative to first available closing price
        start_price = data['Close'].iloc[0]
        pct_change = ((data['Close'] - start_price) / start_price) * 100

        plt.plot(data.index, pct_change, label=ticker)

        # Total percentage change over the period
        total_change = pct_change.iloc[-1]
        total_changes[ticker] = total_change

    # Print total % change for each stock BEFORE showing the chart
    print("\nTotal Percentage Change over the period:")
    for ticker, change in total_changes.items():
        print(f"{ticker}: {change:.2f}%")

    # Show the chart
    plt.title(f"Stock Percentage Change Over Last {years} Years")
    plt.xlabel("Date")
    plt.ylabel("Percentage Change (%)")
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

    plot_percentage_change(tickers, years)
