import pandas as pd

def compute_pnl(
    returns: pd.Series,
    position: pd.Series
) -> pd.Series:
    """
    Strategy return = position * market return
    """
    return position * returns


def equity_curve(strategy_returns: pd.Series) -> pd.Series:
    """
    Compounded growth of $1
    """
    return (1 + strategy_returns).cumprod()
