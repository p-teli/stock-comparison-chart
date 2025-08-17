import yfinance as yf
from datetime import datetime, timedelta
import plotly.graph_objs as go
from plotly.offline import plot

def plot_percentage_change_interactive(tickers, years):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years*365)
    
    fig = go.Figure()
    total_changes = {}

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        
        if data.empty:
            print(f"No data found for {ticker}")
            continue

        # Calculate percentage change
        start_price = data['Close'].iloc[0]
        pct_change = ((data['Close'] - start_price) / start_price) * 100
        total_changes[ticker] = pct_change.iloc[-1]

        # Add a line to the interactive chart
        fig.add_trace(go.Scatter(
            x=data.index,
            y=pct_change,
            mode='lines+markers',
            name=ticker,
            hovertemplate='%{x|%Y-%m-%d}<br>%{y:.2f}%<extra>'+ticker+'</extra>'
        ))

    # Layout settings
    fig.update_layout(
        title=f'Stock Percentage Change Over Last {years} Years',
        xaxis_title='Date',
        yaxis_title='Percentage Change (%)',
        hovermode='closest'  # <-- shows only hovered line
    )

    # Print total percentage change BEFORE showing chart
    print("\nTotal Percentage Change over the period:")
    for ticker, change in total_changes.items():
        print(f"{ticker}: {change:.2f}%")

    # Save as interactive HTML and open in browser
    plot(fig, filename='stock_comparison.html', auto_open=True)

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

    plot_percentage_change_interactive(tickers, years)
