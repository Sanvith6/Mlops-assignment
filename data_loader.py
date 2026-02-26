from pathlib import Path
from io import StringIO

import pandas as pd


REQUIRED_COLUMNS = {"close"}


def load_data(path: str) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        raise ValueError(f"Invalid CSV file format: {e}")

    # Handle CSVs where each full row is wrapped in quotes, yielding one merged column.
    if len(df.columns) == 1 and "," in str(df.columns[0]):
        try:
            raw_lines = [line.strip() for line in csv_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            normalized_lines = [
                line[1:-1] if len(line) >= 2 and line.startswith('"') and line.endswith('"') else line
                for line in raw_lines
            ]
            df = pd.read_csv(StringIO("\n".join(normalized_lines)))
        except Exception as e:
            raise ValueError(f"Invalid quoted-row CSV format: {e}")

    if df.empty:
        raise ValueError("Input CSV file is empty.")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df
