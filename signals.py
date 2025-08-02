def detect_signals(df):
    signals = []
    for i in range(1, len(df)):
        if df["RSI"].iloc[i] < 30 and df["RSI"].iloc[i-1] >= 30:
            signals.append((df.index[i], "RSI < 30"))
        if df["SMA_50"].iloc[i] > df["SMA_200"].iloc[i] and df["SMA_50"].iloc[i-1] <= df["SMA_200"].iloc[i-1]:
            signals.append((df.index[i], "Golden Cross"))
    return signals
