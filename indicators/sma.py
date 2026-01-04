import pandas as pd

def sma(series: pd.Series, window: int) -> pd.Series:
    """
    Simple Moving Average
    Each value = mean of last `window` prices
    """
    if window <= 0:
        raise ValueError("window must be > 0")

    return series.rolling(window=window).mean()
