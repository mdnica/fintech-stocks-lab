import pandas as pd

def ema(series: pd.Series, window: int) -> pd.Series:
    """
    Exponential Moving Average
    Recent prices matter more than old ones
    """
    if window <= 0:
        raise ValueError("window must be > 0")

    return series.ewm(span=window, adjust=False).mean()
