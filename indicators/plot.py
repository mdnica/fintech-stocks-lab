import matplotlib.pyplot as plt
import pandas as pd

def plot_price_with_indicators(
    df: pd.DataFrame,
    ticker: str,
    price_col: str = "close"
):
    subset = df[df["ticker"] == ticker]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Price + MAs
    axes[0].plot(subset["date"], subset[price_col], label="Price")
    axes[0].plot(subset["date"], subset["sma_20"], label="SMA 20")
    axes[0].plot(subset["date"], subset["ema_20"], label="EMA 20")
    axes[0].set_title(f"{ticker} Price")
    axes[0].legend()

    # RSI
    axes[1].plot(subset["date"], subset["rsi_14"], label="RSI")
    axes[1].axhline(70, linestyle="--", alpha=0.6)
    axes[1].axhline(30, linestyle="--", alpha=0.6)
    axes[1].set_title("RSI")
    axes[1].legend()

    plt.tight_layout()
    plt.show()
