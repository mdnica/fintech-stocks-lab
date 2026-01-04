import pandas as pd

def to_tidy_ohlcv(raw: pd.DataFrame) -> pd.DataFrame:
    """
    Convert yfinance multi-column output into a tidy table:
    date | ticker | open | high | low | close | adj_close | volume
    """
    # yfinance returns:
    # - single ticker: columns like ['Open','High',...]
    # - multi ticker: columns are MultiIndex
    if isinstance(raw.columns, pd.MultiIndex):
        stacked = raw.stack(level=1, future_stack=True).reset_index()

        stacked = stacked.rename(columns={"level_1": "ticker", "Date": "date"})
    else:
        # single ticker fallback
        stacked = raw.reset_index()
        stacked["ticker"] = "SINGLE"
        stacked = stacked.rename(columns={"Date": "date"})

    # normalize column names
    stacked.columns = [c.lower().replace(" ", "_") for c in stacked.columns]

    needed = ["date", "ticker", "open", "high", "low", "close", "adj_close", "volume"]
    missing = [c for c in needed if c not in stacked.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    tidy = stacked[needed].copy()

    # basic cleaning rules
    tidy = tidy.dropna(subset=["close"])
    tidy["volume"] = tidy["volume"].fillna(0).astype("int64")
    tidy = tidy.sort_values(["ticker", "date"])

    return tidy
