import os
import requests
import zipfile
import glob
import pandas as pd

divvy_url = "https://divvy-tripdata.s3.amazonaws.com"
raw_zip_dir = "data/raw/divvy"
raw_csv_dir = "data/raw/divvy_csv"
interim_dir = "data/interim"

os.makedirs(raw_zip_dir, exist_ok=True)
os.makedirs(raw_csv_dir, exist_ok=True)
os.makedirs(interim_dir, exist_ok=True)

def get_months():
    months = []
    year, month = 2024, 5
    while not (year == 2025 and month == 6):
        months.append(f"{year}{month:02d}")
        month += 1
        if month == 13:
            month = 1
            year += 1
    return months

def download_divvy():
    months = get_months()
    for yyyymm in months:
        fname = f"{yyyymm}-divvy-tripdata.zip"
        url = f"{divvy_url}/{fname}"
        out_path = os.path.join(raw_zip_dir, fname)

        if os.path.exists(out_path):
            print("skip:", out_path)
            continue

        print("downloading:", url)
        resp = requests.get(url, stream=True)
        if resp.status_code == 200:
            with open(out_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            print("saved:", out_path)
        else:
            print("failed:", resp.status_code, url)

def extract_zips():
    pattern = os.path.join(raw_zip_dir, "*.zip")
    for zip_path in glob.glob(pattern):
        print("extract:", zip_path)
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(raw_csv_dir)

def build_hourly_demand():
    use_cols = ["started_at", "start_station_id", "start_lat", "start_lng"]
    all_hourly = []

    pattern = os.path.join(raw_csv_dir, "*.csv")
    csv_files = sorted(glob.glob(pattern))
    print("found csv files:", len(csv_files))

    for path in csv_files:
        print("reading:", path)
        df = pd.read_csv(path, usecols=use_cols)
        df["started_at"] = pd.to_datetime(df["started_at"])
        df["hour"] = df["started_at"].dt.floor("H")

        hourly = (
            df.groupby(["start_station_id", "hour"])
              .size()
              .reset_index(name="trips")
        )
        all_hourly.append(hourly)

    combined = pd.concat(all_hourly, ignore_index=True)
    combined = (
        combined.groupby(["start_station_id", "hour"])["trips"]
                .sum()
                .reset_index()
    )

    out_path = os.path.join(interim_dir, "hourly_demand_raw.csv")
    combined.to_csv(out_path, index=False)
    print("saved hourly demand:", out_path)
    print(combined.head())

def main():
    download_divvy()
    extract_zips()
    build_hourly_demand()

if __name__ == "__main__":
    main()
  
