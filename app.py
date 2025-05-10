from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

# Load reasons from a file
def load_reasons():
    file_path = os.path.join(os.path.dirname(__file__), "reasons.txt")
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

# Load solutions from a file
def load_solutions():
    file_path = os.path.join(os.path.dirname(__file__), "solutions.txt")
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

reasons = load_reasons()
solutions = load_solutions()

@app.route("/")
def index():
    # Generate a random reason and solution
    reason = random.choice(reasons)
    solution = random.choice(solutions)
    return render_template("index.html", reason=reason, solution=solution)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
