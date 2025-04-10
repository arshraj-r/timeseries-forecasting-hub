import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima(train_series, order=(1, 1, 1)):
    model = ARIMA(train_series, order=order)
    fitted_model = model.fit()
    return fitted_model

def forecast_arima(model, steps):
    forecast = model.forecast(steps=steps)
    return forecast
