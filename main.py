from data_fetcher import fetch_daily_data
from indicators import add_indicators
from signals import detect_signals
from dotenv import load_dotenv
import os

def main():

    # Cargar .env
    load_dotenv()

    API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not API_KEY:
        raise Exception("Por favor define la variable de entorno ALPHAVANTAGE_API_KEY con tu API key")

    SYMBOL = "SPY"

    df = fetch_daily_data(SYMBOL, API_KEY)
    df = add_indicators(df)
    signals = detect_signals(df)
    print(df.tail(10)[['close', 'RSI', 'SMA_50', 'SMA_200']])


    print(f"Señales detectadas para {SYMBOL}:")
    for date, signal in signals:
        print(f"{date.date()}: {signal}")

if __name__ == "__main__":
    main()
