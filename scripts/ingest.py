"""
Ingest humanitarian datasets (UN OCHA / World Bank).
"""
import pandas as pd
from pathlib import Path

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

if __name__ == "__main__":
    # TODO: replace with real source path
    src = Path("data/sample.csv")
    if src.exists():
        df = load_csv(src)
        print(df.head())
    else:
        print("No data yet. Place CSVs under data/")
