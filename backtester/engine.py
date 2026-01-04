import pandas as pd
import numpy as np

class Backtester:
    def __init__(
        self,
        returns: pd.Series,
        position: pd.Series,
        fee_bps: float = 1.0,
        slippage_bps: float = 1.0,
    ):
        """
        fee_bps: transaction cost in basis points (1 bp = 0.01%)
        slippage_bps: execution slippage in basis points
        """
        self.returns = returns.fillna(0)
        self.position = position.fillna(0)

        self.fee = fee_bps / 10_000
        self.slippage = slippage_bps / 10_000

    def run(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "returns": self.returns,
            "position": self.position
        })

        # Position changes (trades)
        df["trade"] = df["position"].diff().abs()

        # Costs only apply when we trade
        df["cost"] = df["trade"] * (self.fee + self.slippage)

        # Strategy return
        df["strategy_return"] = (
            df["position"] * df["returns"] - df["cost"]
        )

        # Equity curve
        df["equity"] = (1 + df["strategy_return"]).cumprod()

        return df
