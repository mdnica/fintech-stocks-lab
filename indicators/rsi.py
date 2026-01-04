import pandas as pd

def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    """
    Relative Strength Index (RSI)
    Measures momentum between 0 and 100
    """
    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi
