# crypto_robo_advisor
## Algo evolution :
### V1 :
The code first calculates the daily returns by taking the percentage change of the closing price, and then uses the standard deviation of these returns to estimate the volatility. The inverse of this volatility is then used to assign a weight to each asset (less volatility → more weight), and these weights are normalized so that their sum equals 100%.

### V2 :
The algorithm calculates each asset’s daily volatility from its returns, uses the inverse of volatility to favor less volatile assets, and reduces their weight if the RSI is over 70 (indicating overbought conditions). Then it normalizes these weights to sum to 100%, yielding the optimal allocation.

## Definitions :
* **Standard Deviation**: is used as a measure of volatility—it's computed as the square root of the average squared differences of daily returns from their mean.
* **RSI** : Relative Strength Index is a momentum oscillator that measures the speed and change of price movements to identify overbought or oversold market conditions. 
-> Technical Analysis Library in Python (ta)
  
```
Project
```

