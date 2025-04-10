from flask import Flask, render_template
from robo_advisor import run_robo_advisor

app = Flask(__name__)

@app.route('/')
def index():
    # Run the robo-advisor to get the optimal allocations
    allocations = run_robo_advisor()
    return render_template('index.html', allocations=allocations)

if __name__ == '__main__':
    try:
        allocations_result = run_robo_advisor()
    except KeyboardInterrupt:
        print("Operation interrupted by user.")
        raise

    print("Optimal Allocations:")
    for symbol, weight in allocations_result.items():
        print(f"{symbol}: {weight * 100:.2f}%")
    
    app.run(host="0.0.0.0", port=5000, debug=True)
