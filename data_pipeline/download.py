import yfinance as yf
import pandas as pd

def download_prices(tickers: tuple[str, ...], start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """
    Download OHLCV price data for multiple tickers.
    Returns a DataFrame with a DateTime index and columns in a MultiIndex:
    (PriceField, Ticker) like ('Close', 'AAPL').
    """
    df = yf.download(
        tickers=list(tickers),
        start=start,
        end=end,
        interval=interval,
        group_by="column",
        auto_adjust=False,  # keep raw prices (we'll talk about adjust later)
        progress=False,
        threads=True,
    )

    if df.empty:
        raise ValueError("No data returned. Check tickers or date range.")

    # Ensure index is datetime
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    return df
