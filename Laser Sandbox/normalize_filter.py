import pandas as pd

def normalize_and_filter(df: pd.DataFrame) -> pd.DataFrame:
    df["QtyOpen"] = pd.to_numeric(df["QtyOpen"], errors="coerce").fillna(0)
    df["EndDate"] = pd.to_datetime(df["EndDate"], errors="coerce")

    # remove closed / invalid rows
    df = df[df["QtyOpen"] > 0]
    df = df.dropna(subset=["QJ_PartNumber"])

    return df.reset_index(drop=True)
