import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "login_attempts": np.random.randint(1, 5, 100),
    "failed_logins": np.random.randint(0, 3, 100),
    "data_transfer_mb": np.random.randint(50, 200, 100),

    "ip_address": np.random.choice([
        "192.168.1.5",
        "192.168.1.20",
        "192.168.1.30",
        "192.168.1.50"
    ],100),

    "country": np.random.choice([
        "India",
        "USA",
        "Russia",
        "China",
        "Germany"
    ],100)
}

df = pd.DataFrame(data)

# Inject anomalies
df.loc[95, "failed_logins"] = 10
df.loc[96, "failed_logins"] = 12
df.loc[97, "failed_logins"] = 15
df.loc[98, "failed_logins"] = 20

df.loc[95, "data_transfer_mb"] = 500
df.loc[96, "data_transfer_mb"] = 600
df.loc[97, "data_transfer_mb"] = 700
df.loc[98, "data_transfer_mb"] = 800

df.to_csv("security_logs.csv", index=False)

print("Security logs generated successfully!")