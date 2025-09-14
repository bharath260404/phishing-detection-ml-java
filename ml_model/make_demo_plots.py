import numpy as np
import matplotlib.pyplot as plt
import os

# Make sure plots folder exists
os.makedirs('plots', exist_ok=True)

# 1. Synthetic class distribution
counts = [600, 400]  # 60% legit, 40% phishing
plt.figure(figsize=(4,4))
plt.pie(counts, labels=['Legit','Phishing'], autopct='%1.1f%%')
plt.title('Class distribution (demo)')
plt.savefig('plots/class_dist.png', bbox_inches='tight', dpi=150)
plt.close()

# 2. Synthetic URL length histogram
url_lengths = np.random.normal(70, 25, 1000).clip(5,200)
plt.figure(figsize=(5,3))
plt.hist(url_lengths, bins=25)
plt.title('URL length distribution (demo)')
plt.xlabel('URL length (chars)')
plt.ylabel('Count')
plt.savefig('plots/url_length_hist.png', bbox_inches='tight', dpi=150)
plt.close()

# 3. Synthetic feature importance
features = ['url_length','suspicious_words','has_https','is_ip','num_digits']
importances = [0.28,0.22,0.20,0.16,0.14]
plt.figure(figsize=(6,3))
plt.bar(features, importances)
plt.title('Feature importance (demo)')
plt.ylabel('Importance')
plt.savefig('plots/feature_importance.png', bbox_inches='tight', dpi=150)
plt.close()

# 4. Synthetic ROC curve
fpr = [0.0,0.1,0.2,0.4,1.0]
tpr = [0.0,0.6,0.8,0.95,1.0]
plt.figure(figsize=(5,3))
plt.plot(fpr, tpr)
plt.plot([0,1],[0,1],'--')
plt.title('ROC Curve (AUC = 0.92)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.savefig('plots/roc_curve.png', bbox_inches='tight', dpi=150)
plt.close()
