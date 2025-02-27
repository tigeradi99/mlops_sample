from typing import List
import joblib
from flask import Flask, request, jsonify
from pydantic import BaseModel

app = Flask(__name__)

# Load the model
# Define the labels corresponding to the target classes
LABELS = [
    "Verdante",  # A vibrant and fresh wine, inspired by its balanced acidity and crisp flavors.
    "Rubresco",  # A rich and robust wine, named for its deep, ruby color and bold taste profile.
    "Floralis",  # A fragrant and elegant wine, known for its floral notes and smooth finish.
]

class Features(BaseModel):
    features: List[float]

def load_model(file_path):
    return joblib.load(file_path)

model = load_model("model.pkl")

# Home route to display the form
# @app.route("/")
# def home():
#     return render_template("index.html")


# Prediction route to handle form submissions
@app.route("/predict", methods=["POST"])
def predict():
    features_validated: Features = Features(features=request.json["features"])
    # Get the numerical prediction
    prediction_index = model.predict([features_validated.features])[0]
    # Map the numerical prediction to the label
    prediction_label = LABELS[prediction_index]

    # Display the prediction on the same page
    return jsonify({"prediction_text": f"Predicted Wine Class: {prediction_label}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)