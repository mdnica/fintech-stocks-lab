import pandas as pd
import numpy as np

def volatility_target_position(
    raw_position: pd.Series,
    realized_vol: pd.Series,
    target_vol: float = 0.10,
    max_leverage: float = 1.0
) -> pd.Series:
    """
    Scales position so portfolio volatility stays near target.
    """
    scaling = target_vol / realized_vol
    scaling = scaling.clip(upper=max_leverage)

    sized_position = raw_position * scaling
    return sized_position.fillna(0)
