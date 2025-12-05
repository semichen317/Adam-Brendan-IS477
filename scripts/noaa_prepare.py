# %%
import os
import requests
import pandas as pd
import hashlib

noaa_url = "https://www.ncei.noaa.gov/data/global-hourly/access"
raw_dir = "data/raw/noaa"
interim_dir = "data/interim"

os.makedirs(raw_dir, exist_ok=True)
os.makedirs(interim_dir, exist_ok=True)

station = "72530094846"
years = [2024, 2025]
out_raw = os.path.join(interim_dir, "noaa_hourly_raw.csv")
start = pd.Timestamp("2024-05-01")
end = pd.Timestamp("2025-05-31")

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def write_sha(path):
    digest = sha256_of_file(path)
    sha_path = path + ".sha256"
    with open(sha_path, "w") as f:
        f.write(digest)
    print("wrote checksum:", sha_path)

def verify_sha(path):
    sha_path = path + ".sha256"
    if not os.path.exists(sha_path):
        return False
    with open(sha_path) as f:
        recorded = f.read().strip()
    current = sha256_of_file(path)
    return recorded == current


def download_year(year):
    url = f"{noaa_url}/{year}/{station}.csv"
    out_path = os.path.join(raw_dir, f"{year}-{station}.csv")

    if os.path.exists(out_path) and verify_sha(out_path):
        print("exists + checksum OK → skip", out_path)
        return out_path

    print("downloading", url)
    resp = requests.get(url, stream=True, timeout=120)
    if resp.status_code != 200:
        print("failed", resp.status_code)
        return None

    with open(out_path, "wb") as f:
        for chunk in resp.iter_content(1024 * 1024):
            if chunk:
                f.write(chunk)

    write_sha(out_path)
    return out_path

def build_raw():
    paths = []
    for y in years:
        p = download_year(y)
        if p:
            paths.append(p)

    frames = []
    for p in paths:
        print("read", p)
        df = pd.read_csv(p)
        if "DATE" not in df.columns:
            continue
        df["datetime"] = pd.to_datetime(df["DATE"])
        m = (df["datetime"] >= start) & (df["datetime"] <= end)
        df = df.loc[m]
        frames.append(df)

    if not frames:
        print("no data")
        return

    df = pd.concat(frames, ignore_index=True)
    keep_cols = [c for c in ["datetime", "TMP", "DEW", "SLP", "WND", "AA1"] if c in df.columns]
    df = df[keep_cols]

    df.to_csv(out_raw, index=False)
    print("saved", out_raw)
    print(df.head())

def main():
    build_raw()
if __name__ == "__main__":
    main()


