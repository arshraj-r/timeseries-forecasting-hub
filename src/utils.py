import matplotlib.pyplot as plt

def plot_series(series, title="Time Series", xlabel="Date", ylabel="Value"):
    plt.figure(figsize=(10, 4))
    plt.plot(series)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_forecast(train, test, forecast, title="Forecast vs Actual"):
    plt.figure(figsize=(12, 5))
    plt.plot(train, label='Train')
    plt.plot(test, label='Actual')
    plt.plot(forecast, label='Forecast')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
