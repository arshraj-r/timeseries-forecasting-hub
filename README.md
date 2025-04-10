
# 📈 Time Series Forecasting Hub

A comprehensive repository exploring various time series forecasting models, from traditional statistical techniques to advanced deep learning architectures. The goal is to build, test, and compare forecasting methods across multiple datasets to better understand their strengths and use cases.

---

## 🔍 Project Goals

- Explore and implement **statistical**, **machine learning**, and **deep learning** models for time series forecasting.
- Benchmark multiple models on diverse datasets.
- Learn popular open-source libraries used in the industry.
- Serve as a go-to reference for time series forecasting experiments.

---

## 🧠 Models Covered

### ✅ Classical Statistical Models
- AR, MA, ARMA
- ARIMA, SARIMA, SARIMAX
- Holt-Winters Exponential Smoothing
- ETS (Error-Trend-Seasonality models)

### ✅ Machine Learning Models
- Linear Regression with lag features
- Random Forest Regressor
- XGBoost, LightGBM
- Support Vector Regression (SVR)

### ✅ Deep Learning Models
- LSTM, GRU
- 1D CNN
- TCN (Temporal Convolutional Network)
- Transformer-based models (e.g. Informer, TimesNet)

### ✅ Hybrid & Libraries
- Facebook Prophet
- NeuralProphet
- Darts
- GluonTS
- PyTorch Forecasting
- Nixtla: `statsforecast`, `mlforecast`, `hierarchicalforecast`

---

## 📂 Directory Structure

```bash
ts-forecasting-hub/
│
├── data/                # Raw and processed datasets
│   ├── raw/
│   └── processed/
│
├── notebooks/           # Jupyter notebooks for EDA and model training
│
├── models/              # Model-specific scripts
│   ├── arima/
│   ├── prophet/
│   ├── lstm/
│   └── transformer/
│
├── src/                 # Utility scripts
│   ├── preprocessing.py
│   ├── evaluation.py
│   ├── utils.py
│   └── dataloader.py
│
├── results/             # Forecast results and plots
│
├── experiments/         # Configs for reproducible experiments
│
├── requirements.txt     # Python dependencies
└── README.md            # Project overview
```

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/arshraj-r/timeseries-forecasting-hub.git
cd ttimeseries-forecasting-hub

# Install dependencies
pip install -r requirements.txt
```

Alternatively, you can set up a Conda environment using `environment.yml`.

---

## 📊 Datasets Used

- Airline Passengers
- Daily Energy Consumption
- Sunspots
- Stock Prices (Yahoo Finance)
- Temperature and Weather Time Series
- Synthetic or custom datasets (user-defined)

---

## 📈 Evaluation Metrics

- MAE - Mean Absolute Error
- RMSE - Root Mean Squared Error
- MAPE - Mean Absolute Percentage Error
- sMAPE - Symmetric Mean Absolute Percentage Error
- Plots: Forecast vs. Actual

---

## 🚧 Project Status

| Task                             | Status     |
|----------------------------------|------------|
| Setup classical models           | ✅ Complete |
| Prophet + NeuralProphet          | ✅ Complete |
| Machine learning models          | ⏳ In Progress |
| Deep learning (LSTM, TCN, etc.)  | ⏳ In Progress |
| Transformer-based models         | 🔜 Planned |
| Model comparison dashboard       | 🔜 Planned |
| Hyperparameter tuning (Optuna)   | 🔜 Planned |

---

## 📚 Resources

- [Darts Docs](https://github.com/unit8co/darts)
- [Facebook Prophet](https://facebook.github.io/prophet/)
- [PyTorch Forecasting](https://pytorch-forecasting.readthedocs.io/)
- [GluonTS by AWS](https://gluon-ts.mxnet.io/)
- [Nixtla Forecasting Libraries](https://github.com/Nixtla)

---

## 🤝 Contributions

Contributions are welcome! If you'd like to add new models, fix bugs, or suggest features, feel free to open an issue or pull request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💡 Author

Maintained by **[Arshraj Randhawa](https://github.com/arshraj-r)**
