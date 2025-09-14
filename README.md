🛡️ Phishing Attack Detection using Machine Learning & Java

## About
Phishing is the most common social engineering attack where fake websites trick people into sharing sensitive information.  
In this project we built:  
- 🧠 A Machine Learning model to classify phishing vs. safe websites  
- 💻 A simple Java program to quickly flag suspicious URLs with heuristic rules  

## Dataset
We used publicly available datasets:  
- Kaggle → [Phishing Dataset for Machine Learning](https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning)  
- UCI → [Phishing Websites Dataset](https://archive.ics.uci.edu/ml/datasets/phishing+websites)  

## How to Run

### 1. Train ML Model

cd ml_model
python train_and_save.py
Output:

model.pkl → saved ML model

plots/ → ROC curve, Feature Importance, Class Distribution charts

2. Run Java Demo
bash
Copy code
cd java_demo
javac SimplePhishingCheck.java
java SimplePhishingCheck
Example:

sql
Copy code
Enter URL: http://login-free-bank-secure.com
----- Analysis for: http://login-free-bank-secure.com
Risk score: 6.0   Risk level: HIGH
Reasons: Contains suspicious word: 'login'. Contains suspicious word: 'bank'.
🚨 Recommendation: Treat as PHISHING.
Results
Random Forest Accuracy ≈ 95%

Precision ≈ 94%

Recall ≈ 96%

ROC AUC ≈ 0.92

Future Scope
Deploy ML model as REST API for real-time detection

Build browser extension / email filter

Add QR-code and mobile phishing detection

Contributors
Bharath Jella
