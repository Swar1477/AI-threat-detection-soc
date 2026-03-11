import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="AI Threat Detection SOC", layout="wide")

st.title("🛡 AI Threat Detection SOC Dashboard")
st.subheader("Cybersecurity Threat Monitoring System")

df = pd.read_csv("detected_threats.csv")

total_logs = len(df)
threats = df[df["anomaly"] == "Suspicious"]

col1, col2 = st.columns(2)

col1.metric("Total Logs", total_logs)
col2.metric("Suspicious Events", len(threats))

st.write("---")

st.subheader("Threat Dataset")
st.dataframe(df)

st.write("---")

# Threat Distribution Graph
st.subheader("Threat Detection Results")

fig, ax = plt.subplots()

counts = df["anomaly"].value_counts()

ax.bar(counts.index, counts.values)

ax.set_xlabel("Type")
ax.set_ylabel("Count")

st.pyplot(fig)

st.write("---")

# Suspicious events
st.subheader("Suspicious Activities")

suspicious = df[df["anomaly"] == "Suspicious"]

st.dataframe(suspicious)

st.write("---")

# TOP ATTACKER DETECTION

st.subheader("Top Attacker Detection")

if "ip_address" in df.columns:

    top_ip = df["ip_address"].value_counts().idxmax()

    st.error(f"🚨 Top Attacker IP: {top_ip}")

else:
    st.info("IP tracking not enabled yet")

st.write("---")

#global attackmap
st.subheader("Global Attack Map")

if "country" in df.columns:

    country_counts = df["country"].value_counts().reset_index()
    country_counts.columns = ["country","attacks"]

    st.bar_chart(country_counts.set_index("country"))

else:
    st.info("Country tracking not enabled")


# SEVERITY LEVEL

st.subheader("Threat Severity")

def severity(row):
    if row["failed_logins"] > 15:
        return "HIGH"
    elif row["failed_logins"] > 5:
        return "MEDIUM"
    else:
        return "LOW"

df["severity"] = df.apply(severity, axis=1)

st.dataframe(df[["failed_logins","severity"]])

st.write("---")

# ATTACK TIMELINE

st.subheader("Attack Timeline")

timeline = df["failed_logins"]

fig2, ax2 = plt.subplots()

ax2.plot(timeline)

ax2.set_xlabel("Log Index")
ax2.set_ylabel("Failed Login Attempts")

st.pyplot(fig2)

st.write("---")

# LIVE ATTACK SIMULATION

st.subheader("Live Attack Simulation")

placeholder = st.empty()

for i in range(5):

    fake_attack = random.randint(5,20)

    placeholder.warning(f"⚠ New attack detected — Failed logins: {fake_attack}")

    time.sleep(2)

st.success("Simulation finished")