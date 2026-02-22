from flask import Flask, render_template, request, jsonify
from model import predict_resilience

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/simulator")
def simulator():
    return render_template("simulator.html")


@app.route("/predict", methods=["POST"])
def predict():

    temp = float(request.form["temperature"])
    rain = float(request.form["rainfall"])
    pop = float(request.form["population_density"])

    prediction, climate_type, status, actions = predict_resilience(temp, rain, pop)

    return jsonify({
        "score": prediction,
        "climate": climate_type,
        "status": status,
        "actions": actions
    })


if __name__ == "__main__":
    app.run(debug=True)