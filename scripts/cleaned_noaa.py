# %%
import os
import pandas as pd
import numpy as np

raw_path = "data/interim/noaa_hourly_raw.csv"
out_path = "data/cleaned/noaa_hourly_clean.csv"
os.makedirs("data/cleaned", exist_ok=True)

def parse_tmp(v):
    if isinstance(v, str) and len(v) >= 4 and v[:4] != "9999":
        return int(v[:4]) / 10.0
    return np.nan

def parse_wnd_speed(v):
    if isinstance(v, str) and len(v) >= 5 and v[:5] != "99999":
        v = v.replace(",", ".")
        return float(v[3:5])
    return np.nan

def parse_aa1_precip(v):
    if not isinstance(v, str) or len(v) < 8:
        return np.nan
    depth = v[4:8]
    depth = depth.replace(",", ".")
    if depth == "9999":
        return np.nan
    return float(depth) / 10.0

df = pd.read_csv(raw_path)
if "datetime" not in df.columns and "DATE" in df.columns:
    df["datetime"] = pd.to_datetime(df["DATE"])
else:
    df["datetime"] = pd.to_datetime(df["datetime"])
df["hour"] = df["datetime"].dt.floor("H")

if "TMP" in df.columns:
    df["temp_c"] = df["TMP"].apply(parse_tmp)
else:
    df["temp_c"] = np.nan

if "WND" in df.columns:
    df["wind_ms"] = df["WND"].apply(parse_wnd_speed)
else:
    df["wind_ms"] = np.nan

if "AA1" in df.columns:
    df["precip_mm"] = df["AA1"].apply(parse_aa1_precip)
else:
    df["precip_mm"] = np.nan

keep = ["hour", "temp_c", "wind_ms", "precip_mm"]
df2 = df[keep].drop_duplicates(subset=["hour"]).sort_values("hour")
df2.to_csv(out_path, index=False)

print("saved: ", out_path)
df2.head()

# %%



