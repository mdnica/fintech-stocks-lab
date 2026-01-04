import pandas as pd

def sma_crossover_signal(
    fast: pd.Series,
    slow: pd.Series
) -> pd.Series:
    """
    Returns:
    1  -> buy signal
    0  -> no position
    """
    signal = (fast > slow).astype(int)
    return signal
