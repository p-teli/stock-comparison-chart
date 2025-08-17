import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_stock_price(company, years):
    # Calculate start date
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years*365)

    # Fetch historical stock data
    stock = yf.Ticker(company)
    data = stock.history(start=start_date, end=end_date)

    if data.empty:
        print("No data found for this company or time period.")
        return

    # Plot closing price
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.title(f"{company} Stock Price for Last {years} Years")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.legend()
    plt.show()

# Main
if __name__ == "__main__":
    company = input("Enter company ticker (e.g., AAPL, MSFT): ").upper()
    years = int(input("Enter number of years: "))
    plot_stock_price(company, years)
