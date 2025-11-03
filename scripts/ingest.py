import os
import pandas as pd

RAW_PATH = "data/sample_humanitarian_data.csv"
CLEAN_DIR = "data/cleaned"
CLEAN_PATH = os.path.join(CLEAN_DIR, "humanitarian_clean.csv")

def ensure_dirs():
    os.makedirs(CLEAN_DIR, exist_ok=True)

def load_data(path):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    return df

def clean_data(df):
    df = df.dropna(subset=["country", "year", "aid_type", "amount_usd"])
    df["country"] = df["country"].str.title().str.strip()
    df["aid_type"] = df["aid_type"].str.title().str.strip()
    df["organization"] = df["organization"].fillna("Unknown").str.title()
    return df

def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    print("Starting ingestion...")
    ensure_dirs()
    df = load_data(RAW_PATH)
    df_clean = clean_data(df)
    save_data(df_clean, CLEAN_PATH)
    print(f"Saved cleaned data to {CLEAN_PATH}")

if __name__ == "__main__":
    main()
