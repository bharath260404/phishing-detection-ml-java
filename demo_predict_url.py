import joblib
import pandas as pd

# Load trained model
model = joblib.load("model_simple.pkl")

# Must match training script exactly
FEATURES = ["UrlLength", "AtSymbol", "IpAddress", "NoHttps"]

def extract_features(url: str) -> dict:
    # UrlLength = number of characters
    url_length = len(url)

    # AtSymbol = 1 if "@" in URL
    at_symbol = 1 if "@" in url else 0

    # IpAddress = 1 if domain part looks like an IP
    try:
        domain = url.split("/")[2]
        ip_address = 1 if all(part.isdigit() for part in domain.split(".") if part) else 0
    except:
        ip_address = 0

    # NoHttps = 1 if not starting with https
    no_https = 0 if url.lower().startswith("https") else 1

    return {
        "UrlLength": url_length,
        "AtSymbol": at_symbol,
        "IpAddress": ip_address,
        "NoHttps": no_https,
    }

print("🔎 Phishing URL Detector (ML Model)")
print("Type a URL to check (or 'exit' to quit):")

while True:
    url = input("\nEnter URL: ").strip()
    if url.lower() == "exit":
        print("Exiting... Stay safe online! 🛡️")
        break

    feats = extract_features(url)
    X = pd.DataFrame([feats], columns=FEATURES)

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[:,1][0]

    print(f"\nFeatures: {feats}")
    print(f"Prediction: {'🚨 Phishing' if pred==1 else '✅ Safe'}")
    print(f"Probability of phishing: {prob:.2f}")
