import pandas as pd

def load_csv(path, datetime_column=None):
    df = pd.read_csv(path)

    if datetime_column:
        df[datetime_column] = pd.to_datetime(df[datetime_column])
        df.set_index(datetime_column, inplace=True)
        df.index.freq = pd.infer_freq(df.index)

    return df
