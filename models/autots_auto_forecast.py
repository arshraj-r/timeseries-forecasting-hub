from autots import AutoTS

def run_autots_forecast(df, forecast_length=14, date_col=None, value_col=None):
    model = AutoTS(
        forecast_length=forecast_length,
        frequency='infer',
        ensemble='simple',
    )
    if date_col and value_col:
        df = df[[date_col, value_col]].rename(columns={date_col: 'datetime', value_col: 'value'})
        df = df.set_index('datetime')

    df = df.asfreq(df.index.inferred_freq or 'D')
    model = model.fit(df, date_col=None, value_col=None, id_col=None)
    prediction = model.predict()
    forecast = prediction.forecast
    return forecast
