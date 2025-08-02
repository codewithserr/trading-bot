import pandas_ta as ta
import pandas as pd

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df['RSI'] = ta.rsi(df['close'], length=14)
    df['SMA_50'] = ta.sma(df['close'], length=50)
    df['SMA_200'] = ta.sma(df['close'], length=200)
    return df
