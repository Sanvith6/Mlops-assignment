from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"timestamp", "open", "high", "low", "close"}


def load_data(path: str) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        raise ValueError(f"Invalid CSV file format: {e}")

    if df.empty:
        raise ValueError("Input CSV file is empty.")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df
