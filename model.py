import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("sample_data.csv")

# Features
X = data[["temperature", "rainfall", "population_density"]]

# Target
y = data["resilience_score"]

# Train model
model = LinearRegression()
model.fit(X, y)


def detect_climate(temp, rain):
    if rain > 250:
        return "cyclone"
    elif temp > 40:
        return "heatwave"
    elif rain < 50:
        return "drought"
    else:
        return "normal"


def generate_actions(climate_type, score):

    base_actions = []

    if score < 40:
        base_actions.append("Emergency preparedness programs")
        base_actions.append("Strengthen disaster response systems")

    if climate_type == "cyclone":
        base_actions.extend([
            "Coastal barrier reinforcement",
            "Storm-resistant housing",
            "Evacuation route planning"
        ])

    elif climate_type == "heatwave":
        base_actions.extend([
            "Increase urban green cover",
            "Cooling shelters",
            "Water conservation systems"
        ])

    elif climate_type == "drought":
        base_actions.extend([
            "Rainwater harvesting",
            "Drought-resistant crops",
            "Water storage planning"
        ])

    else:
        base_actions.extend([
            "Maintain infrastructure monitoring",
            "Community awareness programs"
        ])

    return base_actions


def predict_resilience(temp, rain, pop):

    input_data = pd.DataFrame(
        [[temp, rain, pop]],
        columns=["temperature", "rainfall", "population_density"]
    )

    prediction = model.predict(input_data)[0]

    # Keep between 0–100
    prediction = max(0, min(100, prediction))
    prediction = round(prediction, 2)

    climate_type = detect_climate(temp, rain)

    if prediction < 40:
        status = "Low Resilience – High Risk"
    elif prediction < 70:
        status = "Moderate Resilience – Needs Improvement"
    else:
        status = "High Resilience – Strong Stability"

    actions = generate_actions(climate_type, prediction)

    return prediction, climate_type, status, actions