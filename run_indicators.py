import pandas as pd
from indicators.sma import sma
from indicators.ema import ema
from indicators.rsi import rsi
from indicators.plot import plot_price_with_indicators

DATA_PATH = "data/stocks_ohlcv_returns.parquet"

def main():
    df = pd.read_parquet(DATA_PATH)

    # choose ONE stock to visualize
    ticker = "AAPL"

    df.loc[df["ticker"] == ticker, "sma_20"] = sma(
        df[df["ticker"] == ticker]["close"], 20
    )

    df.loc[df["ticker"] == ticker, "ema_20"] = ema(
        df[df["ticker"] == ticker]["close"], 20
    )

    df.loc[df["ticker"] == ticker, "rsi_14"] = rsi(
        df[df["ticker"] == ticker]["close"], 14
    )

    plot_price_with_indicators(df, ticker)

if __name__ == "__main__":
    main()
