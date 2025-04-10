from data_collector import get_binance_data
import pandas as pd
import matplotlib.pyplot as plt

def backtest_strategy(symbol, period=365):
    """
    Backtests a strategy for the given trading pair over a specified period.
    
    This function fetches historical data for the specified symbol over 'period' days,
    computes daily returns and the cumulative return.
    
    :param symbol: Trading pair, e.g., 'BTC/USDT'
    :param period: Number of days to include in the backtest (default is 365).
    :return: A DataFrame with columns 'date', 'close', 'returns', and 'cumulative_return'
    """
    # Fetch historical OHLCV data from Binance.
    df = get_binance_data(symbol, limit=period)
    
    # Calculate daily returns.
    df['returns'] = df['close'].pct_change()
    
    # Calculate the cumulative return of the asset.
    df['cumulative_return'] = (1 + df['returns']).cumprod()
    return df

if __name__ == '__main__':
    # Run a backtest for BTC/USDT over the last 365 days
    df_backtest = backtest_strategy('BTC/USDT', period=365)
    
    # Calculate percentage returns from the cumulative factor
    df_backtest['return_percent'] = (df_backtest['cumulative_return'] - 1) * 100
    
    # Display the last rows of the backtest results.
    print(df_backtest[['date', 'close', 'return_percent']].tail())
    
    # Plot the return percentage
    plt.figure(figsize=(10, 5))
    plt.plot(df_backtest['date'], df_backtest['return_percent'], label='Return (%)')
    plt.xlabel('Date')
    plt.ylabel('Return (%)')
    plt.title('Backtest: BTC/USDT Return (%) Over 365 Days')
    plt.legend()
    plt.grid(True)
    plt.show()
