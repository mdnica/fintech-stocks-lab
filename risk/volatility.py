import pandas as pd
import numpy as np

TRADING_DAYS = 252

def rolling_volatility(
    returns: pd.Series,
    window: int = 20
) -> pd.Series:
    """
    Annualized rolling volatility
    """
    return returns.rolling(window).std() * np.sqrt(TRADING_DAYS)
