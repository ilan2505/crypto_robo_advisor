import ccxt
import pandas as pd
import matplotlib.pyplot as plt
from data_collector import get_binance_data

# Fetch data for BTC/USDT (for example, 100 days)
df_btc = get_binance_data('BTC/USDT', limit=100)

# Plot the closing price of BTC/USDT
plt.figure(figsize=(10, 5))
plt.plot(df_btc['date'], df_btc['close'], label='BTC/USDT')
plt.xlabel('Date')
plt.ylabel('Closing Price (USDT)')
plt.title('BTC/USDT Price Evolution')
plt.legend()
plt.grid(True)
plt.show()
