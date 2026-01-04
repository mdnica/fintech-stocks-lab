import numpy as np
import pandas as pd

def add_returns(tidy: pd.DataFrame) -> pd.DataFrame:
    """
    Adds:
    - simple_return: (P_t / P_{t-1}) - 1
    - log_return: ln(P_t / P_{t-1})
    Computed per ticker WITHOUT breaking the index.
    """
    df = tidy.copy()

    df["simple_return"] = (
        df.groupby("ticker")["close"]
        .transform(lambda s: s.pct_change())
    )

    df["log_return"] = (
        df.groupby("ticker")["close"]
        .transform(lambda s: np.log(s / s.shift(1)))
    )

    return df
