# crypto_robo_advisor
## Algo evolution :
### V1 :
The code first calculates the daily returns by taking the percentage change of the closing price, and then uses the standard deviation of these returns to estimate the volatility. The inverse of this volatility is then used to assign a weight to each asset (less volatility → more weight), and these weights are normalized so that their sum equals 100%.


```
Project
```

