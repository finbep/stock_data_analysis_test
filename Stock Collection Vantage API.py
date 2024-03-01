from alpha_vantage.timeseries import TimeSeries
import pandas as pd


def fetch_hourly_stock_data(api_key, symbol):
    """
    Fetch hourly stock data for a given symbol using the Alpha Vantage API.

    :param api_key: Your Alpha Vantage API key as a string.
    :param symbol: The stock symbol to fetch data for.
    :return: DataFrame with the stock data.
    """
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol, interval='60min', outputsize='full')
    
    # Rename columns to be more descriptive
    data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    
    return data

def save_data_to_csv(data, filename):
    """
    Save the DataFrame to a CSV file.

    :param data: The DataFrame containing the stock data.
    :param filename: The name of the CSV file to save the data.
    """
    data.to_csv(filename)
    print(f'Data saved to {filename}')

# Your Alpha Vantage API key
api_key = 'YOUR_API_KEY_HERE'

# Stock symbol to fetch data for
symbol = 'AAPL'  # Example: Apple Inc.

# Fetch the stock data
stock_data = fetch_hourly_stock_data(api_key, symbol)

# Filename to save the data
filename = 'AAPL_hourly_stock_data.csv'

# Save the fetched data to a CSV file
save_data_to_csv(stock_data, filename)
