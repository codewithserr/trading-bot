import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt
from signals import detect_signals

symbol = "SPY"
data = yf.download(symbol, start="2022-01-01", end="2025-08-01")

data["RSI"] = ta.rsi(data["Close"], length=14)
data["SMA_50"] = ta.sma(data["Close"], length=50)
data["SMA_200"] = ta.sma(data["Close"], length=200)

signals = detect_signals(data)
for date, signal in signals:
    print(f"{date.date()} - Señal detectada: {signal}")

data[["Close", "SMA_50", "SMA_200"]].plot(figsize=(12, 6))
plt.title(f"{symbol} con SMA 50 y 200")
plt.grid()
plt.show()
