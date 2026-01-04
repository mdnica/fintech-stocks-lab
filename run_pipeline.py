from data_pipeline.config import Config
from data_pipeline.download import download_prices
from data_pipeline.clean import to_tidy_ohlcv
from data_pipeline.features import add_returns
from data_pipeline.storage import save_parquet, save_csv
from pathlib import Path

def main() -> None:
    cfg = Config()

    raw = download_prices(cfg.tickers, cfg.start, cfg.end, cfg.interval)
    tidy = to_tidy_ohlcv(raw)
    final = add_returns(tidy)

    out_dir = Path(cfg.data_dir)
    save_parquet(final, out_dir / "stocks_ohlcv_returns.parquet")
    save_csv(final, out_dir / "stocks_ohlcv_returns.csv")

    print("✅ Done!")
    print(f"Rows: {len(final):,}")
    print(f"Saved to: {out_dir.resolve()}")

if __name__ == "__main__":
    main()
