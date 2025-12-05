# %%
import os
import pandas as pd
import numpy as np

"""os.chdir("/Users/brendanspeckmann/Desktop/IS477")"""

cleaned_path_noaa = "data/cleaned/noaa_hourly_clean.csv"
cleaned_path_divvy = "data/cleaned/hourly_demand_clean.csv"
out_path = "data/interim/integrated_dataset.csv"

df_noaa = pd.read_csv(cleaned_path_noaa)
df_divvy = pd.read_csv(cleaned_path_divvy)

df = df_divvy.merge(df_noaa, on="hour", how="left")
    
df.to_csv(out_path, index=False)
print("saved:", out_path)

# %%
df.head()


