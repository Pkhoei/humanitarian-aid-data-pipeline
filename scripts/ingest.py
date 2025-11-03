import argparse
import pandas as pd

def clean_title(s: pd.Series) -> pd.Series:
    return s.fillna("Unknown").astype(str).str.strip().str.title()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="path to raw csv")
    p.add_argument("--output", required=True, help="path to cleaned csv")
    p.add_argument("--year-min", type=int, default=2000)
    p.add_argument("--year-max", type=int, default=2030)
    args = p.parse_args()

    df = pd.read_csv(args.input)

    # rename if needed (flexible)
    rename_map = {
        "Country": "country",
        "Year": "year",
        "AidType": "aid_type",
        "Organization": "organization",
        "AmountUSD": "amount_usd",
        "Region": "region",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    # required columns
    required = ["country", "year", "aid_type", "amount_usd"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # clean
    df["country"] = clean_title(df["country"])
    df["aid_type"] = clean_title(df["aid_type"])
    if "organization" in df.columns:
        df["organization"] = clean_title(df["organization"])
    else:
        df["organization"] = "Unknown"

    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["amount_usd"] = pd.to_numeric(df["amount_usd"], errors="coerce")

    # rules
    df = df.dropna(subset=["country", "year", "aid_type", "amount_usd"])
    df = df[(df["year"] >= args.year_min) & (df["year"] <= args.year_max)]
    df = df[df["amount_usd"] >= 0]
    df = df.drop_duplicates()

    # save
    df.to_csv(args.output, index=False)
    print(f"✅ Saved cleaned dataset → {args.output} (rows={len(df)})")

if __name__ == "__main__":
    main()
