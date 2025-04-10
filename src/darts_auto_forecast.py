from darts.models import NBEATSModel
from darts import TimeSeries
from darts.utils.timeseries_generation import datetime_attribute_timeseries
from darts.dataprocessing.transformers import Scaler

def run_darts_nbeats(series, forecast_horizon=12):
    ts = TimeSeries.from_series(series)
    scaler = Scaler()
    ts_scaled = scaler.fit_transform(ts)

    model = NBEATSModel(input_chunk_length=30, output_chunk_length=forecast_horizon, random_state=42)
    model.fit(ts_scaled, verbose=False)

    forecast = model.predict(forecast_horizon)
    return scaler.inverse_transform(forecast)
