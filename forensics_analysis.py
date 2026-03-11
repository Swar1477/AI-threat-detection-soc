import pandas as pd

df = pd.read_csv("parsed_logs.csv")

failed = df[df["login_status"] == "failed"]

top_ip = failed["ip_address"].value_counts().idxmax()

print("\nForensic Report")
print("----------------------")

print("Top attacking IP:", top_ip)

print("\nFailed login attempts per IP:")
print(failed["ip_address"].value_counts())

if failed["ip_address"].value_counts().max() > 3:
    print("⚠️ ALERT: Possible brute force attack detected")