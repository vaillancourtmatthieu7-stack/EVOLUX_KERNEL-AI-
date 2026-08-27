from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/world")
def world():
    random.seed(42)
    buildings=[]
    for i in range(45):
        buildings.append({
            "x": random.uniform(-35,35),
            "z": random.uniform(-35,35),
            "w": random.uniform(2,6),
            "h": random.uniform(2,14),
            "d": random.uniform(2,6)
        })
    return jsonify({"buildings":buildings})

app.run(host="127.0.0.1", port=8787)
