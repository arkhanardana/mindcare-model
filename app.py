from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

# Load model
with open("mental_model_advanced.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)

def yes_no_to_int(value):
    return 1 if str(value).lower() in ["yes", "1", "true"] else 0

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        age = float(data.get("age"))
        sleep_hours = float(data.get("sleep_hours"))
        work_hours = float(data.get("work_hours"))
        feels_anxious = yes_no_to_int(data.get("feels_anxious"))
        has_support = yes_no_to_int(data.get("has_support"))
        eats_well = yes_no_to_int(data.get("eats_well"))
        physical_activity = yes_no_to_int(data.get("physical_activity"))
        uses_social_media_hours = float(data.get("uses_social_media_hours"))
        has_sleep_disorder = yes_no_to_int(data.get("has_sleep_disorder"))
        satisfaction_level = int(data.get("satisfaction_level"))

        features = [[
            age, sleep_hours, work_hours, feels_anxious, has_support, eats_well,
            physical_activity, uses_social_media_hours, has_sleep_disorder, satisfaction_level
        ]]

        prediction = model.predict(features)[0]
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
