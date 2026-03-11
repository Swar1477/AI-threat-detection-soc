import pandas as pd
import random
import time

file = "security_logs.csv"

while True:

    new_log = {
        "login_attempts": random.randint(1,5),
        "failed_logins": random.randint(0,20),
        "data_transfer_mb": random.randint(50,900)
    }

    df = pd.read_csv(file)

    df.loc[len(df)] = new_log

    df.to_csv(file,index=False)

    print("New log generated:", new_log)

    time.sleep(10)