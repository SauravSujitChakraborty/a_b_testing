import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, brier_score_loss

# 1. SYNTHETIC MARKET DATA GENERATION ==========================================
# Indicator Function: Y = 1(x0 * x1 + x2 > 0.8)
np.random.seed(42)
n_samples = 1000
X = np.random.rand(n_samples, 5) 

# Features 0, 1, 2 are Signal; 3 and 4 are Market Noise
y = (X[:, 0] * X[:, 1] + X[:, 2] > 0.8).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. THE DUEL: LOGISTIC REG (Linear) VS. RANDOM FOREST (Non-Linear) =============
# Baseline Logistic Regression (Has High Bias on non-linear data)
legacy_model = LogisticRegression()
legacy_model.fit(X_train, y_train)

# Random Forest (Has Lower Bias, captures interactions)
challenger_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
challenger_model.fit(X_train, y_train)

# 3. QUANT AUDIT: SIGNAL & NOISE ANALYSIS ======================================
print("--- Logistic Regression vs Random Forest --\n")

def audit_model(model, X_t, y_t, name):
    preds = model.predict(X_t)
    probs = model.predict_proba(X_t)[:, 1]
    
    # Brier Score measures the accuracy of PROBABILITIES
    calibration = brier_score_loss(y_t, probs)
    
    print(f"[{name} PERFORMANCE]")
    print(classification_report(y_t, preds))
    print(f"Signal Calibration (Brier Score): {calibration:.4f}")
    print("-" * 30)

audit_model(legacy_model, X_test, y_test, "LOGISTIC REGRESSION")
audit_model(challenger_model, X_test, y_test, "RANDOM FOREST")

# 4. FEATURE ATTRIBUTION =======================================================
importances = challenger_model.feature_importances_
print("\n[FEATURE ANALYSIS]")
for i, val in enumerate(importances):
    status = "SIGNAL" if i < 3 else "NOISE"
    print(f"Feature X{i} ({status}): {val:.4f}")

# 5. ERROR ANALYSIS (Confusion Matrix) =========================================
cm = confusion_matrix(y_test, challenger_model.predict(X_test))
print("\n--- Random Forest Error Analysis ---")
print(f"False Positives (Costly Mistakes): {cm[0][1]}")
print(f"False Negatives (Missed Alpha): {cm[1][0]}")
