import pandas as pd

def apply_drawdown_stop(
    equity: pd.Series,
    position: pd.Series,
    max_dd: float = -0.20
) -> pd.Series:
    """
    Stops trading if drawdown breaches limit.
    """
    peak = equity.cummax()
    drawdown = (equity - peak) / peak

    stopped = position.copy()
    stopped[drawdown <= max_dd] = 0

    return stopped
