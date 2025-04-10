from prophet import Prophet
import pandas as pd

def prepare_prophet_df(df, column_name):
    return df.reset_index().rename(columns={column_name: 'y', df.index.name or 'index': 'ds'})

def train_prophet(df):
    model = Prophet()
    model.fit(df)
    return model

def forecast_prophet(model, periods, freq='D'):
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]
