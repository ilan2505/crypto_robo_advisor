from data_collector import get_binance_data
from optimizer import allocate_portfolio

def run_robo_advisor():
    """
    Execute data collection and calculate improved portfolio allocations
    using both inverse volatility and RSI adjustments.
    
    :return: A dictionary with asset allocations.
    """
    symbols = ['BTC/USDT', 'ETH/USDT']
    data_dict = {}
    for symbol in symbols:
        print(f"Fetching data for {symbol} ...")
        data_dict[symbol] = get_binance_data(symbol)
    
    print("Calculating improved allocations...")
    allocations = allocate_portfolio(data_dict)
    return allocations

if __name__ == '__main__':
    allocations_result = run_robo_advisor()
    print("Improved Optimal Allocations:")
    for symbol, weight in allocations_result.items():
        print(f"{symbol}: {weight * 100:.2f}%")
