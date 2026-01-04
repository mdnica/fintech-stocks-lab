import pandas as pd
import matplotlib.pyplot as plt

from indicators.sma import sma
from strategies.signals import sma_crossover_signal
from strategies.positions import position_from_signal

from backtester.engine import Backtester
from backtester.metrics import cagr, sharpe_ratio, max_drawdown

from risk.volatility import rolling_volatility
from risk.position_sizing import volatility_target_position
from risk.limits import apply_drawdown_stop

DATA_PATH = "data/stocks_ohlcv_returns.parquet"

def main():
    df = pd.read_parquet(DATA_PATH)
    ticker = "SPY"

    data = df[df["ticker"] == ticker].copy()

    # Strategy
    data["sma_fast"] = sma(data["close"], 20)
    data["sma_slow"] = sma(data["close"], 50)

    data["signal"] = sma_crossover_signal(
        data["sma_fast"], data["sma_slow"]
    )
    raw_position = position_from_signal(data["signal"])

    # Risk layer
    data["vol"] = rolling_volatility(data["simple_return"], 20)
    sized_position = volatility_target_position(
        raw_position,
        data["vol"],
        target_vol=0.10
    )

    # Temporary backtest (before stop)
    bt_temp = Backtester(
        returns=data["simple_return"],
        position=sized_position
    )
    temp_results = bt_temp.run()

    # Drawdown stop
    final_position = apply_drawdown_stop(
        temp_results["equity"],
        sized_position,
        max_dd=-0.20
    )

    # Final backtest
    bt = Backtester(
        returns=data["simple_return"],
        position=final_position
    )
    results = bt.run()

    # Metrics
    print("CAGR:", round(cagr(results["equity"]) * 100, 2), "%")
    print("Sharpe:", round(sharpe_ratio(results["strategy_return"]), 2))
    print("Max Drawdown:", round(max_drawdown(results["equity"]) * 100, 2), "%")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(results["equity"], label="Strategy with Risk Engine")
    plt.title("SMA Strategy with Risk Controls — SPY")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
