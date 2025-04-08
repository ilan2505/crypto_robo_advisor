import ccxt
import pandas as pd

def get_binance_data(symbol='BTC/USDT', timeframe='1d', since=None, limit=365):
    """
    Fetch OHLCV data from Binance for a given trading pair.
    
    :param symbol: Trading pair (e.g., 'BTC/USDT')
    :param timeframe: Time interval (e.g., '1d' for daily)
    :param since: Timestamp in milliseconds from which to start fetching data (optional)
    :param limit: Number of data points to retrieve (days)
    :return: A pandas DataFrame with columns: timestamp, open, high, low, close, volume, and date.
    """
    exchange = ccxt.binance()
    if since is None:
        # Retrieve data for the last 'limit' days
        since = exchange.milliseconds() - limit * 24 * 60 * 60 * 1000
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Test the function with BTC/USDT
df_btc = get_binance_data('BTC/USDT')
df_btc.head()
