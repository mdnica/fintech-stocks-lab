import pandas as pd

def position_from_signal(signal: pd.Series) -> pd.Series:
    """
    Shift signal by 1 to avoid look-ahead bias.
    You can only trade AFTER you see the signal.
    """
    return signal.shift(1).fillna(0)
