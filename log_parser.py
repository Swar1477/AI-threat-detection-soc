import pandas as pd
import re

# sample log file
log_file = "auth.log"

records = []

pattern = r'(\w+\s+\d+\s+\d+:\d+:\d+).*from\s([\d\.]+)'

with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)
            ip = match.group(2)

            status = "failed" if "Failed password" in line else "success"

            records.append({
                "timestamp": timestamp,
                "ip_address": ip,
                "login_status": status
            })

df = pd.DataFrame(records)

df.to_csv("parsed_logs.csv", index=False)

print("Logs parsed successfully!")