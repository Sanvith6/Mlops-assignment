import pandas as pd


def compute_signals(df: pd.DataFrame, window: int) -> tuple[pd.Series, pd.Series]:
    rolling_mean = df["close"].rolling(window=window, min_periods=1).mean()
    signals = (df["close"] > rolling_mean).astype(int)
    return rolling_mean, signals
