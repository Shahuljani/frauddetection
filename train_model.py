import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/creditcard.csv")

print("Columns:", df.columns)

# Target column
target_col = "isFraud"

# Drop non-useful ID columns
df.drop(["nameOrig", "nameDest"], axis=1, inplace=True)

# Encode transaction type
le = LabelEncoder()
df["type"] = le.fit_transform(df["type"])

# Split features & target
X = df.drop(target_col, axis=1)
y = df[target_col]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model, scaler, encoder
with open("model/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("model/type_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model, scaler, and encoder saved successfully")
