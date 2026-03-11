import pandas as pd
import matplotlib.pyplot as plt

# Load detected threats
df = pd.read_csv("detected_threats.csv")

# Count anomalies vs normal
counts = df["anomaly"].value_counts()

# Plot
plt.figure()
counts.plot(kind="bar")

plt.title("Threat Detection Results")
plt.xlabel("Event Type")
plt.ylabel("Count")

plt.show()