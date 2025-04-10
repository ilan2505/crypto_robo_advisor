import pandas as pd
import matplotlib.pyplot as plt
from data_collector import get_binance_data

def backtest_portfolio(allocations, period=365):
    """
    Backtests a multi-asset portfolio based on the given allocations over a specified period.
    
    This function fetches historical data for each trading pair over 'period' days,
    calculates daily returns for each asset, combines them according to their weights (allocations),
    and computes the cumulative portfolio value.
    """
    # Dictionary to hold individual asset DataFrames
    dfs = {}
    for symbol in allocations.keys():
        df = get_binance_data(symbol, limit=period)
        # Calculate daily returns (fill the first missing value with 0)
        df['returns'] = df['close'].pct_change().fillna(0)
        # Keep only 'date' and 'returns'; rename returns column to uniquely identify the asset
        df = df[['date', 'returns']].copy()
        df.rename(columns={'returns': f"returns_{symbol.replace('/', '_')}"}, inplace=True)
        # Set 'date' as index for merging later
        dfs[symbol] = df.set_index('date')
    
    # Merge all individual DataFrames on their date index; fill missing values with 0
    portfolio_df = pd.concat(dfs.values(), axis=1, join='outer').fillna(0)
    
    # Compute weighted daily returns based on allocations
    weighted_returns = 0
    for symbol, allocation in allocations.items():
        col_name = f"returns_{symbol.replace('/', '_')}"
        weighted_returns += portfolio_df[col_name] * allocation
    
    portfolio_df['weighted_returns'] = weighted_returns
    # Calculate cumulative portfolio value starting with 1
    portfolio_df['portfolio_value'] = (1 + portfolio_df['weighted_returns']).cumprod()
    
    return portfolio_df

if __name__ == '__main__':
    # Example allocations: 60% for BTC/USDT and 40% for ETH/USDT.
    allocations = {
        'BTC/USDT': 0.6,
        'ETH/USDT': 0.4
    }
    
    # Run the backtest for a period of 365 days.
    portfolio = backtest_portfolio(allocations, period=365)
    
    # Compute the portfolio return in percentage.
    portfolio['portfolio_return_percent'] = (portfolio['portfolio_value'] - 1) * 100
    
    # Print the last few rows of the portfolio return.
    print(portfolio[['portfolio_return_percent']].tail())
    
    # Create a figure for plotting.
    plt.figure(figsize=(12, 8))
    
    # Plot overall portfolio return in percentage (black, thicker line).
    plt.plot(portfolio.index, portfolio['portfolio_return_percent'],
             label='Portfolio Return (%)', linewidth=3, color='black')
    
    # Compute and plot the individual cumulative returns for BTC/USDT.
    if 'returns_BTC_USDT' in portfolio.columns:
        btc_cum = (1 + portfolio['returns_BTC_USDT']).cumprod()
        btc_return_percent = (btc_cum - 1) * 100
        plt.plot(portfolio.index, btc_return_percent, label='BTC/USDT Return (%)')
    
    # Compute and plot the individual cumulative returns for ETH/USDT.
    if 'returns_ETH_USDT' in portfolio.columns:
        eth_cum = (1 + portfolio['returns_ETH_USDT']).cumprod()
        eth_return_percent = (eth_cum - 1) * 100
        plt.plot(portfolio.index, eth_return_percent, label='ETH/USDT Return (%)')
    
    plt.xlabel('Date')
    plt.ylabel('Return (%)')
    plt.title('Multi-Asset Portfolio Backtest (Return in Percentage)')
    plt.legend()
    plt.grid(True)
    plt.show()
