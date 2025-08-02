import requests
import pandas as pd

def fetch_daily_data(symbol: str, api_key: str) -> pd.DataFrame:
    """
    Descarga datos diarios sin ajustar desde Alpha Vantage (versión gratuita).
    """
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_DAILY&symbol={symbol}"
        f"&outputsize=full&apikey={api_key}"
    )

    print(f"Descargando datos de {symbol} desde Alpha Vantage (JSON)...")
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error al conectar: {response.status_code}")

    data = response.json()

    if "Time Series (Daily)" not in data:
        print("⚠️ Respuesta inesperada de la API:")
        print(data)
        raise Exception("La clave 'Time Series (Daily)' no está presente. Puede ser una API key inválida, símbolo incorrecto, o límite alcanzado.")

    raw = data["Time Series (Daily)"]

    df = pd.DataFrame.from_dict(raw, orient="index", dtype=float)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    }, inplace=True)

    return df
