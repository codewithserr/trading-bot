import pandas as pd

def detect_signals(df: pd.DataFrame):
    signals = []
    df = df.dropna(subset=['RSI', 'SMA_50', 'SMA_200'])

    for i in range(1, len(df)):
        # RSI cruces
        if df['RSI'].iloc[i] < 30 and df['RSI'].iloc[i-1] >= 30:
            signals.append((df.index[i], 'BUY - RSI Oversold'))
        elif df['RSI'].iloc[i] > 70 and df['RSI'].iloc[i-1] <= 70:
            signals.append((df.index[i], 'SELL - RSI Overbought'))

        # Golden/Death Cross SMA
        if (df['SMA_50'].iloc[i] > df['SMA_200'].iloc[i]) and (df['SMA_50'].iloc[i-1] <= df['SMA_200'].iloc[i-1]):
            signals.append((df.index[i], 'BUY - Golden Cross'))
        elif (df['SMA_50'].iloc[i] < df['SMA_200'].iloc[i]) and (df['SMA_50'].iloc[i-1] >= df['SMA_200'].iloc[i-1]):
            signals.append((df.index[i], 'SELL - Death Cross'))

    return signals
