import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import joblib

# Load dataset
DATASET_PATH = "../dataset/phishing.csv"
print("🔎 Loading dataset...")
df = pd.read_csv(DATASET_PATH)

# Choose simplified feature set (matches what we can compute from URLs)
FEATURES = ["UrlLength", "AtSymbol", "IpAddress", "NoHttps"]
TARGET = "CLASS_LABEL"

X = df[FEATURES]
y = df[TARGET]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🔎 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
roc = roc_auc_score(y_test, y_prob)

print("\n✅ Model Evaluation:")
print(f"Accuracy: {acc:.2f}")
print(f"Precision: {prec:.2f}")
print(f"Recall: {rec:.2f}")
print(f"ROC AUC: {roc:.2f}")

# Save model
joblib.dump(model, "model_simple.pkl")
print("\n💾 Model saved as model_simple.pkl")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import joblib

# Load dataset
DATASET_PATH = "../dataset/phishing.csv"
print("🔎 Loading dataset...")
df = pd.read_csv(DATASET_PATH)

# Choose simplified feature set (matches what we can compute from URLs)
FEATURES = ["UrlLength", "AtSymbol", "IpAddress", "NoHttps"]
TARGET = "CLASS_LABEL"

X = df[FEATURES]
y = df[TARGET]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🔎 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
roc = roc_auc_score(y_test, y_prob)

print("\n✅ Model Evaluation:")
print(f"Accuracy: {acc:.2f}")
print(f"Precision: {prec:.2f}")
print(f"Recall: {rec:.2f}")
print(f"ROC AUC: {roc:.2f}")

# Save model
joblib.dump(model, "model_simple.pkl")
print("\n💾 Model saved as model_simple.pkl")
