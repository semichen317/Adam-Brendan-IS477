# %%
import os
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

from sklearn.model_selection import train_test_split

import seaborn as sns
import matplotlib.pyplot as plt


"""os.chdir("/Users/brendanspeckmann/Desktop/IS477")"""

df = pd.read_csv("data/interim/integrated_dataset.csv")

df = df.dropna(axis=0, how="any")

df["station_id_encoded"] = df["start_station_id"].astype("category").cat.codes
df["hour"] = pd.to_datetime(df["hour"])
df["hour_of_day"] = df["hour"].dt.hour
df["day_of_week"] = df["hour"].dt.dayofweek
df["month"] = df["hour"].dt.month

df = df.drop("hour", axis = 1)
df = df.drop("start_station_id", axis=1)

df_sample = df.sample(frac=0.5, random_state=42)
feature_cols = ["station_id_encoded", "temp_c", "wind_ms", "precip_mm", "hour_of_day", "day_of_week", "month"]
X = df_sample[feature_cols]
y = df_sample["trips"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=.2,
    random_state = 42
)

tree = RandomForestRegressor(random_state=42, n_estimators = 200)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

baseline_pred = np.full_like(y_test, y_train.mean(), dtype=float)
baseline_rmse = root_mean_squared_error(y_test, baseline_pred)
print("baseline_rmse: ", baseline_rmse)
print("post analysis rmse: ", root_mean_squared_error(y_test, y_pred))

numeric_cols = ["trips", "temp_c", "wind_ms", "precip_mm"]

df_corr = df[numeric_cols].corr()

plt.figure(figsize=(6,4))
sns.heatmap(df_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap: Trips vs Weather")
plt.savefig("figures/correlation_heatmap.png", dpi=300)
plt.show()

plt.figure(figsize=(7,6))

plt.scatter(y_test, y_pred, alpha=0.3)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         "r--", linewidth=2)

plt.xlim(0, 50)
plt.ylim(0, 50)

plt.xlabel("Actual Trips")
plt.ylabel("Predicted Trips")
plt.title("Actual vs Predicted Trips")
plt.grid(True)
plt.savefig("figures/actual_vs_predicted.png", dpi=300)
plt.show()


