from flask import Flask, render_template, request
import random
import os
from services_mapping import service_to_verb_file  # Import the dictionary from the new module

app = Flask(__name__)

# Load components from individual files
def load_component(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

# Load reasons dynamically using verb group files
def load_reasons():
    services = load_component("services.txt")
    reasons = []
    for service in services:
        verb_file = service_to_verb_file.get(service, "verbs_general.txt")
        verbs = load_component(verb_file)
        for verb in verbs:
            reasons.append(f"The fucking {service} {verb}.")
    return reasons

# Load solutions from a file
def load_solutions():
    file_path = os.path.join(os.path.dirname(__file__), "solutions_general.txt")
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

reasons = load_reasons()
solutions = load_solutions()

@app.route("/")
def index():
    # Generate a random service, verb, and solution
    service = random.choice(load_component("services.txt"))
    verb_file = service_to_verb_file.get(service, "verbs_general.txt")
    verb = random.choice(load_component(verb_file))
    
    # Always use the general solutions file
    solution_file = "solutions_general.txt"
    solution = random.choice(load_component(solution_file))
    
    return render_template("index.html", service=service, verb=verb, solution=solution)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host="0.0.0.0", port=port, debug=False)  # Enable debug mode
