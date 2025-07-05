
# day_14_workshop.py

"""
Workshop: Monitoring and Continuous Retraining in ML

This script simulates:
- Model prediction
- Logging ground truth
- Calculating error metrics (MAE)
- Drift detection (based on rolling metrics)
- Trigger retraining if threshold exceeded
- Status feedback (CI/CD style)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# Simulate time-series prediction and ground truth
np.random.seed(42)
days = pd.date_range(start='2024-01-01', periods=60)
actual = np.random.normal(loc=200, scale=10, size=60)
predicted = actual + np.random.normal(loc=0, scale=5, size=60)

df = pd.DataFrame({'date': days, 'actual': actual, 'predicted': predicted})
df['abs_error'] = np.abs(df['actual'] - df['predicted'])

# Calculate 7-day rolling MAE
df['rolling_MAE'] = df['abs_error'].rolling(window=7).mean()

# Drift Trigger Rule
baseline_mae = df['abs_error'][:14].mean()
df['drift'] = df['rolling_MAE'] > (baseline_mae * 1.25)

# Show if retraining should trigger
drift_triggered = df['drift'].rolling(window=3).sum() >= 3

print("Baseline MAE:", baseline_mae)
print("Drift Trigger Threshold:", baseline_mae * 1.25)
print("Retraining Triggered:", drift_triggered.any())

# Plotting MAE and drift
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['rolling_MAE'], label='7-day Rolling MAE')
plt.axhline(baseline_mae * 1.25, color='red', linestyle='--', label='Drift Threshold')
plt.title('Drift Detection: Rolling MAE')
plt.xlabel('Date')
plt.ylabel('MAE')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('rolling_mae_plot.png')
plt.show()
