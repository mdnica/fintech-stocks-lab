# 📊 FinTech Stocks Lab — Project 1

## Market Data Pipeline (Stocks)

This project is the first building block of a **fintech / quantitative trading system**.

It downloads historical **stock market data**, cleans it into a tidy format, computes **returns**, and stores the result in a professional, analysis-ready format.

---

## 🎯 Project Goal

Build a reusable **market data pipeline** that can later feed:

- trading strategies
- backtesting engines
- risk models
- portfolio optimization

This mirrors the **data layer** used in real trading platforms.

---

---

## 📈 Data Source

- Yahoo Finance (via `yfinance`)
- Assets: US stocks and ETFs (e.g. AAPL, MSFT, SPY)

---

## 🧮 Features Created

For each ticker:

- OHLCV prices
- Simple returns
- Log returns

Returns are computed **per ticker**, making the dataset suitable for quantitative analysis.

---

## ▶️ How to Run

### 1. Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt


3. Run the pipeline
   python run_pipeline.py

4. Output
files are saved to:

data/
├── stocks_ohlcv_returns.parquet
└── stocks_ohlcv_returns.csv


👩‍💻 Author - MD Nica

Built as part of a fintech / quant learning journey using Python.

```
