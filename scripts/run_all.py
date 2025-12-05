# %%
import os

"""os.chdir("/Users/brendanspeckmann/Desktop/IS477")"""

os.system("python scripts/prepare/noaa_prepare.py")
os.system("python scripts/prepare/divvy_prepare.py")
os.system("python scripts/cleaned/cleaned_noaa.py")
os.system("python scripts/cleaned/cleaned_divvy.py")
os.system("python scripts/integrated/integrated_script.py")
os.system("python scripts/analysis/analysis.py")


