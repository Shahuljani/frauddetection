from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained objects
model = pickle.load(open("model/fraud_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
encoder = pickle.load(open("model/type_encoder.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        predicted=False,
        prediction_text=""
    )

@app.route("/predict", methods=["POST"])
def predict():
    # Read inputs
    step = float(request.form["step"])
    tx_type = request.form["type"]
    amount = float(request.form["amount"])
    oldbalanceOrg = float(request.form["oldbalanceOrg"])
    newbalanceOrig = float(request.form["newbalanceOrig"])
    oldbalanceDest = float(request.form["oldbalanceDest"])
    newbalanceDest = float(request.form["newbalanceDest"])

    # -------------------------------
    # RULE-BASED FRAUD DETECTION
    # -------------------------------
    if (
        amount > 200000 and
        tx_type in ["TRANSFER", "CASH_OUT"] and
        newbalanceOrig == 0 and
        oldbalanceDest == 0
    ):
        result = "⚠️ Fraudulent Transaction "

    else:
        # -------------------------------
        # MACHINE LEARNING PREDICTION
        # -------------------------------
        tx_type_encoded = encoder.transform([tx_type])[0]
        isFlaggedFraud = 0  # default for user input

        features = [[
            step,
            tx_type_encoded,
            amount,
            oldbalanceOrg,
            newbalanceOrig,
            oldbalanceDest,
            newbalanceDest,
            isFlaggedFraud
        ]]

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)

        result = (
            "⚠️ Fraudulent Transaction (ML Prediction)"
            if prediction[0] == 1
            else "✅ Legitimate Transaction"
        )

    return render_template(
        "index.html",
        predicted=True,
        prediction_text=result
    )

if __name__ == "__main__":
    app.run(debug=True)
