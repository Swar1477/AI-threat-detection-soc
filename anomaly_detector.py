import pandas as pd
from sklearn.ensemble import IsolationForest

# Load logs
df = pd.read_csv("security_logs.csv")

# Features used for detection
features = df[["login_attempts", "failed_logins", "data_transfer_mb"]]

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)

df["anomaly"] = model.fit_predict(features)

# Convert -1 to anomaly label
df["anomaly"] = df["anomaly"].map({1: "Normal", -1: "Suspicious"})

# Show suspicious rows
print("\nDetected Threats:\n")
print(df[df["anomaly"] == "Suspicious"])

# Save results
df.to_csv("detected_threats.csv", index=False)

print("\nDetection completed. Results saved to detected_threats.csv")