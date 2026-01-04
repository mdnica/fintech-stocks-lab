from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Config:
    # A starter list: mix of mega-cap + ETF (nice for learning)
    tickers: tuple[str, ...] = ("AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "TSLA", "SPY")

    # Where we save data
    data_dir: Path = Path("data")

    # Dates: you can change these anytime
    start: str = "2018-01-01"
    end: str = "2025-12-31"

    # Interval: 1d is perfect for first quant projects
    interval: str = "1d"
