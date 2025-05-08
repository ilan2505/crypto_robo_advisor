# crypto_robo_advisor
## Algo evolution :
### V1 :
This algorithm calculates the daily returns by taking the percentage change of the closing price, and then uses the standard deviation of these returns to estimate the volatility. The inverse of this volatility is then used to assign a weight to each asset (less volatility → more weight), and these weights are normalized so that their sum equals 100%.

### V2 :
This algorithm calculates each asset’s daily volatility from its returns, uses the inverse of volatility to favor less volatile assets, and reduces their weight if the RSI is over 70 (indicating overbought conditions). Then it normalizes these weights to sum to 100%, yielding the optimal allocation.

## V3 :
This algorithm computes an optimal allocation by estimating the covariance matrix using an Exponentially Weighted Moving Average (EWMA) and then applying Ledoit–Wolf shrinkage to improve its stability. It then solves a classic mean–variance optimization to maximize risk-adjusted returns for the given assets.

## Definitions :
* **Standard Deviation**: is used as a measure of volatility—it's computed as the square root of the average squared differences of daily returns from their mean.
* **RSI**: Relative Strength Index is a momentum oscillator that measures the speed and change of price movements to identify overbought or oversold market conditions. 
* **EWMA (Exponentially Weighted Moving Average)**: A method to estimate variances and covariances by giving more weight to recent observations and exponentially decaying weights to older data, which makes the estimate more responsive to recent market changes.
* **Ledoit–Wolf shrinkage**: A technique to improve the estimation of the covariance matrix by “shrinking” the sample covariance toward a well-conditioned target (often the identity matrix), reducing estimation error when the number of observations is limited relative to the number of assets.
* **Mean–Variance Optimization**: A framework introduced by Harry Markowitz that finds the portfolio weights minimizing variance for a given expected return (or equivalently maximizing return for a given risk), solving a quadratic programming problem.
* **Shrinkage**: In statistics, combining a noisy estimate (like the sample covariance) with a structured target to reduce overall estimation error.
* **Risk-Adjusted Return (e.g. Sharpe Ratio)**: A measure of return per unit of risk, often used as the objective in portfolio optimization. V3 maximizes a similar metric by balancing expected returns against the portfolio’s volatility.
  
```
Project
```

