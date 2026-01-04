import pandas as pd
import numpy as np

TRADING_DAYS = 252

def cagr(equity: pd.Series) -> float:
    total_years = len(equity) / TRADING_DAYS
    return equity.iloc[-1] ** (1 / total_years) - 1

def annualized_vol(returns: pd.Series) -> float:
    return returns.std() * np.sqrt(TRADING_DAYS)

def sharpe_ratio(returns: pd.Series, risk_free: float = 0.0) -> float:
    excess = returns - risk_free / TRADING_DAYS
    return excess.mean() / excess.std() * np.sqrt(TRADING_DAYS)

def max_drawdown(equity: pd.Series) -> float:
    peak = equity.cummax()
    drawdown = (equity - peak) / peak
    return drawdown.min()
