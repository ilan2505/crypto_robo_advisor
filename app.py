from flask import Flask, render_template
from robo_advisor import run_robo_advisor

app = Flask(__name__)

@app.route('/')
def index():
    # Run the robo-advisor to get the optimal allocations
    allocations = run_robo_advisor()
    return render_template('index.html', allocations=allocations)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
