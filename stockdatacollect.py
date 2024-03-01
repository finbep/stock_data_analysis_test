import yfinance as yf
import pandas as pd

# Function to fetch historical stock data
def fetch_stock_data(stock_symbol, start_date, end_date):
    """
    Fetch historical hourly stock data for a given symbol.

    :param stock_symbol: The ticker symbol for the stock, e.g., 'AAPL' for Apple.
    :param start_date: The start date for fetching data in 'YYYY-MM-DD' format.
    :param end_date: The end date for fetching data in 'YYYY-MM-DD' format.
    :return: A DataFrame with the historical stock data.
    """
    # Fetch the data
    data = yf.download(tickers=stock_symbol, start=start_date, end=end_date, interval='1h')

    # Reset the index to make 'Datetime' a column
    data.reset_index(inplace=True)

    # Select only the required columns
    data = data[['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']]

    return data


# Change these variables to fetch different stocks or different time periods
stock_symbol = 'AAPL'  # Stock symbol
start_date = '2010-05-01'  # Start date
end_date = '2024-02-01'  # End date

# Fetch the stock data
stock_data = fetch_stock_data(stock_symbol, start_date, end_date)

# Display the first few rows of the data
print(stock_data.head())