import pandas as pd
import matplotlib.pyplot as plt

from indicators.sma import sma
from strategies.signals import sma_crossover_signal
from strategies.positions import position_from_signal
from strategies.pnl import compute_pnl, equity_curve

DATA_PATH = "data/stocks_ohlcv_returns.parquet"

def main():
    df = pd.read_parquet(DATA_PATH)

    ticker = "SPY"
    data = df[df["ticker"] == ticker].copy()

    # indicators
    data["sma_fast"] = sma(data["close"], 20)
    data["sma_slow"] = sma(data["close"], 50)

    # signals & positions
    data["signal"] = sma_crossover_signal(
        data["sma_fast"], data["sma_slow"]
    )
    data["position"] = position_from_signal(data["signal"])

    # PnL
    data["strategy_return"] = compute_pnl(
        data["simple_return"], data["position"]
    )
    data["equity"] = equity_curve(data["strategy_return"])

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(data["date"], data["equity"], label="Strategy")
    plt.title(f"SMA Crossover Strategy — {ticker}")
    plt.ylabel("Equity ($)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
