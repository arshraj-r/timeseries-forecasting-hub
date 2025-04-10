import pandas as pd
from sklearn.preprocessing import StandardScaler

def parse_datetime(df, column):
    df[column] = pd.to_datetime(df[column])
    return df

def set_datetime_index(df, column):
    df = df.set_index(column)
    df.index.freq = pd.infer_freq(df.index)
    return df

def scale_series(series):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(series.values.reshape(-1, 1))
    return scaled, scaler