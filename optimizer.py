import pandas as pd
import ta

# def allocate_portfolio(data_dict):
#     """
#     V1 : Calculate the optimal portfolio allocations for cryptocurrencies 
#     based on historical volatility (standard deviation of daily returns).
#     """
#     volatilities = {}
#     for symbol, df in data_dict.items():
#         df['returns'] = df['close'].pct_change()
#         volatilities[symbol] = df['returns'].std()
    
#     # Invert the volatility so that less volatile assets get a higher weight
#     inv_vol = {symbol: 1/vol if vol != 0 else 0 for symbol, vol in volatilities.items()}
#     total_inv_vol = sum(inv_vol.values())
#     allocations = {symbol: inv_vol[symbol] / total_inv_vol for symbol in inv_vol.keys()}
#     return allocations

#-----------------------------------------------------------------------------------------------

def calculate_rsi(df, window=14):
    """
    V2 : Compute the Relative Strength Index (RSI) for the given DataFrame.

    :param df: A DataFrame containing the 'close' prices.
    :param window: The number of periods for RSI calculation (default is 14).
    :return: A pandas Series with the RSI values.
    """
    rsi_indicator = ta.momentum.RSIIndicator(close=df['close'], window=window)
    return rsi_indicator.rsi()

def allocate_portfolio(data_dict):
    """
    V2 : Calculate the optimal portfolio allocations by combining inverse volatility
    with an adjustment for RSI. If the asset's RSI is above 70 (overbought), its weight
    is reduced.

    :param data_dict: A dictionary where each key is a trading pair and the value is a DataFrame with 'close' prices.
    :return: A dictionary with the allocation (weight) for each asset, summing to 1.
    """
    volatilities = {}
    rsi_values = {}

    # Calculate daily returns, volatility, and RSI for each asset.
    for symbol, df in data_dict.items():
        df['returns'] = df['close'].pct_change()
        volatilities[symbol] = df['returns'].std()
        rsi_values[symbol] = calculate_rsi(df).iloc[-1]

    # Compute inverse volatility weights and adjust if RSI is high (over 70).
    inv_vol = {}
    for symbol, vol in volatilities.items():
        weight = 1 / vol if vol != 0 else 0
        if rsi_values[symbol] > 70:
            weight /= 1.2  # Adjust factor; you can change 1.2 as needed.
        inv_vol[symbol] = weight

    total_inv_vol = sum(inv_vol.values())
    allocations = {symbol: inv_vol[symbol] / total_inv_vol for symbol in inv_vol.keys()}
    return allocations
