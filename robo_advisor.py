from data_collector import get_binance_data
from optimizer import allocate_portfolio


def run_robo_advisor():
    """
    Execute data collection and calculate the optimal portfolio allocations for a list of cryptocurrencies.
    """
    symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT']
    data_dict = {}
    for symbol in symbols:
        print(f"Fetching data for {symbol} ...")
        data_dict[symbol] = get_binance_data(symbol)
    
    print("Calculating optimal allocations...")
    allocations = allocate_portfolio(data_dict)
    return allocations

# Run the robo-advisor and display the results
allocations_result = run_robo_advisor()

print("Optimal Allocations:")
for symbol, weight in allocations_result.items():
    print(f"{symbol}: {weight * 100:.2f}%")
