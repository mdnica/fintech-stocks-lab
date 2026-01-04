import pandas as pd
import matplotlib.pyplot as plt

from indicators.sma import sma
from strategies.signals import sma_crossover_signal
from strategies.positions import position_from_signal
from backtester.engine import Backtester
from backtester.metrics import cagr, sharpe_ratio, max_drawdown

DATA_PATH = "data/stocks_ohlcv_returns.parquet"

def main():
    df = pd.read_parquet(DATA_PATH)
    ticker = "SPY"

    data = df[df["ticker"] == ticker].copy()

    # Indicators
    data["sma_fast"] = sma(data["close"], 20)
    data["sma_slow"] = sma(data["close"], 50)

    # Signals & positions
    data["signal"] = sma_crossover_signal(
        data["sma_fast"], data["sma_slow"]
    )
    data["position"] = position_from_signal(data["signal"])

    # Backtest
    bt = Backtester(
        returns=data["simple_return"],
        position=data["position"],
        fee_bps=1.0,
        slippage_bps=1.0
    )

    results = bt.run()

    # Metrics
    print("CAGR:", round(cagr(results["equity"]) * 100, 2), "%")
    print("Sharpe:", round(sharpe_ratio(results["strategy_return"]), 2))
    print("Max Drawdown:", round(max_drawdown(results["equity"]) * 100, 2), "%")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(results.index, results["equity"], label="Strategy (net)")
    plt.title("Backtested SMA Crossover — SPY")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
