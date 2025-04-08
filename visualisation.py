import matplotlib.pyplot as plt

# Plot the closing price of BTC/USDT
plt.figure(figsize=(10, 5))
plt.plot(df_btc['date'], df_btc['close'], label='BTC/USDT')
plt.xlabel('Date')
plt.ylabel('Closing Price (USDT)')
plt.title('BTC/USDT Price Evolution')
plt.legend()
plt.grid(True)
plt.show()

