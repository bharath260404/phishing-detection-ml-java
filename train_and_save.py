# train_and_save.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, classification_report
import joblib
import os

os.makedirs("ml_model/plots", exist_ok=True)

# 1) Load dataset - update filename if needed
df = pd.read_csv("../dataset/phishing.csv")  # path relative to ml_model folder

# 2) Basic preprocessing: assume 'class' or 'label' column
if 'class' in df.columns:
    target = 'class'
elif 'label' in df.columns:
    target = 'label'
else:
    # adjust this if columns differ
    target = df.columns[-1]

X = df.drop(columns=[target])
y = df[target]

# (Optional) Simple feature selection if dataset has many non-numeric columns
# For Kaggle dataset this may already be numeric; otherwise do encoding
# Here we attempt to convert non-numeric to numeric via simple methods if present
for c in X.columns:
    if X[c].dtype == 'object':
        X[c] = X[c].astype('category').cat.codes

# 3) Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# 4) Train RandomForest
rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

# 5) Evaluate
y_pred = rf.predict(X_test)
y_prob = rf.predict_proba(X_test)[:,1]
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
report = classification_report(y_test, y_pred, zero_division=0)

print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1:", f1)
print(report)

# 6) Save model
joblib.dump(rf, "model.pkl")
print("Saved model to ml_model/model.pkl")

# 7) Save plots
# class distribution pie
counts = y.value_counts().sort_index()
plt.figure(figsize=(4,4))
plt.pie(counts, labels=[str(i) for i in counts.index], autopct='%1.1f%%')
plt.title("Class distribution")
plt.savefig("ml_model/plots/class_dist.png", bbox_inches='tight', dpi=150)
plt.close()

# ROC
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(5,3))
plt.plot(fpr, tpr)
plt.plot([0,1],[0,1], linestyle='--')
plt.title(f"ROC Curve (AUC = {roc_auc:.3f})")
plt.xlabel("False Positive Rate"); plt.ylabel("True Positive Rate")
plt.savefig("ml_model/plots/roc_curve.png", bbox_inches='tight', dpi=150)
plt.close()

# Feature importance
importances = rf.feature_importances_
feat_names = X.columns
idx = np.argsort(importances)[::-1]
plt.figure(figsize=(6,3))
plt.bar([feat_names[i] for i in idx[:10]], importances[idx[:10]])
plt.title("Top 10 Feature Importance")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("ml_model/plots/feature_importance.png", bbox_inches='tight', dpi=150)
plt.close()
