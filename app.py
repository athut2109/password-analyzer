from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

from backend.hash_generator import hash_password_to_file
from backend.jtr_wrapper import run_john_dictionaries, check_john_output
from backend.brute_force_simulator import calculate_entropy, estimate_crack_time, get_strength

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    password = data.get("password", "")

    hash_password_to_file(password)
    run_john_dictionaries()
    cracked_password = check_john_output()

    print("🔥 check_john_output() returned:", cracked_password)

    entropy = calculate_entropy(password)
    strength = get_strength(entropy)
    crack_time = estimate_crack_time(entropy)

    if cracked_password:
        suggestions = ["Avoid dictionary words", "Add more complexity"]
        strength = "Weak"
        crack_time = "Instantly"
    else:
        if strength == "Weak":
            suggestions = ["Use a longer password", "Add numbers/symbols"]
        elif strength == "Medium":
            suggestions = ["Use uncommon words", "Add uppercase/symbols"]
        else:
            suggestions = ["Great job!"]

    response = {
        "strength": strength,
        "entropy": f"{entropy:.2f}",
        "crack_time": crack_time,
        "suggestions": suggestions,
        "cracked_by_jtr": bool(cracked_password),
        "cracked_password": cracked_password if cracked_password else "-"
    }

    print("✅ Final response to frontend:", response)
    return jsonify(response)

if __name__ == "__main__":
    os.makedirs("hashes", exist_ok=True)
    app.run(debug=True)
