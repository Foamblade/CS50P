import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for given stock with user-defined start and end dates
def Fetch_Stock_Data(stock, start_date, end_date):
    data = yf.download(stock, start=start_date, end=end_date)
    data['SMA_30'] = data['Close'].rolling(window=30).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    return data

def plot(data):
    # Plotting the stock data and SMAs
    plt.figure(figsize=(10,6))
    plt.plot(data['Close'], label='Stock Close Price', color='black', linewidth=1)
    plt.plot(data['SMA_30'], label='30-Day SMA', color='blue', linewidth=1)
    plt.plot(data['SMA_50'], label='50-Day SMA', color='red', linewidth=1)
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def get_Stock():
    stocks = [
        'AAPL','TSLA','GOOGL','AMZN','MSFT','FB','NFLX',
        'NVDA','PYPL','INTC','ADBE','CSCO','CMCSA','PEP',
        'AVGO','TMUS','COST','QCOM','TXN','AMGN','CHTR',
        'INTU','AMAT','MU','ISRG','GILD','ADP','LRCX','CSX',
        'BIIB','REGN','VRTX','MDLZ','ATVI' 
    ]
    while True:
        stock = input("Enter the stock symbol: ")
        if stock not in stocks:
            print("Stock not found")
        else:
            return stock

def get_dates():
    # Prompt the user for the start and end dates in YYYY-MM-DD format
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Check for valid date format (this is a basic validation)
    try:
        # Attempt to convert the date strings to proper date format
        from datetime import datetime
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the dates in YYYY-MM-DD format.")
        return get_dates()  # Recurse if the date format is incorrect
    
    return start_date, end_date

def trade(data):
    cash = 10000  # Starting cash
    position = 0  # Number of stocks owned

    for i in range(1, len(data)):  # Start at 1 to avoid NaN value at the beginning
        # Skip rows with NaN values for SMA
        if data['SMA_30'].iloc[i] != data['SMA_30'].iloc[i] or data['SMA_50'].iloc[i] != data['SMA_50'].iloc[i]:
            continue
        
        sma_30 = data['SMA_30'].iloc[i]
        sma_50 = data['SMA_50'].iloc[i]
        close_price = data['Close'].iloc[i]

        # Buy signal: When 30-day SMA crosses above 50-day SMA
        if (sma_30 > sma_50) & position == 0:
            position = cash / close_price  # Buy stocks
            cash = 0
            print(f"Bought at {close_price} on {data.index[i]}")

        # Sell signal: When 30-day SMA crosses below 50-day SMA
        elif (sma_30 < sma_50) & position > 0:
            cash = position * close_price  # Sell stocks
            position = 0
            print(f"Sold at {close_price} on {data.index[i]}")

    # Final Portfolio Value (if still holding stocks)
    if position > 0:
        cash = position * data['Close'].iloc[-1]  # Sell at the last price if still holding stocks
        position = 0
        print(f"Sold at {data['Close'].iloc[-1]} on {data.index[-1]}")

    print(f"Final Portfolio Value: ${cash:.2f}")
    return cash


def main():
    stock_symbol = get_Stock()  # Ask for the stock symbol
    start_date, end_date = get_dates()  # Get user-defined start and end dates
    
    # Fetch the stock data for the chosen dates
    data = Fetch_Stock_Data(stock_symbol, start_date, end_date)
    
    print(f"Data for {stock_symbol} from {start_date} to {end_date}:")
    print(data.tail())  # Print last few rows of the data for preview
    
    # Perform trading simulation
    final_value = trade(data)
    
    # Plot the results
    plot(data)

    print(f"Final Portfolio Value after Trading: ${final_value:.2f}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
