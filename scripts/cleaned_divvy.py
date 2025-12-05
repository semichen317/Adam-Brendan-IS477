# %%
import os
import pandas as pd

raw_path = "data/interim/hourly_demand_raw.csv"
out_path = "data/cleaned/hourly_demand_clean.csv"
os.makedirs("data/cleaned", exist_ok=True)


df = pd.read_csv(raw_path)
df = df.dropna(subset=["start_station_id"])
df["start_station_id"] = df["start_station_id"].astype(str).str.strip()
    
df["hour"] = pd.to_datetime(df["hour"])
df["trips"] = pd.to_numeric(df["trips"], errors="coerce")
df = df.dropna(subset="trips")
df = df[df["trips"] > 0]
df = df.sort_values(["start_station_id", "hour"])
    
df.to_csv(out_path, index=False)
print("saved:", out_path)

# %%
df.shape


