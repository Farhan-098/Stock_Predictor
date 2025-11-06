📊 SmartStock Advisor

SmartStock Advisor is a free, AI-powered web app that helps you decide which stocks to Buy, Hold, or Sell — using live data from Yahoo Finance and machine learning trend prediction.

Built entirely with Python + Streamlit, this project showcases how simple ML models can provide valuable insights into market trends, completely free of cost and without API keys.

🌍 Deployed Version

Our app is live and free to use on Streamlit Cloud:

🔗 Visit here: [SmartStock Advisor Live](https://stockpredictor-w2e.streamlit.app/)

🚀 Key Features

✅ Live Stock Tracking — Fetches real-time data via Yahoo Finance
🧠 AI-Based Prediction — Predicts short-term price movements using Linear Regression
🎯 Buy / Hold / Sell Signals — Clear actionable insights for each stock
📈 Visual Trend Charts — Interactive closing price graphs
💸 100% Free & Open Source — Uses only open libraries and public APIs
🌐 Deployed Online — Accessible instantly via Streamlit Cloud

🧠 How It Works

The app fetches the latest stock price data for selected tickers using yfinance.

It trains a Linear Regression model on recent prices to estimate the next day’s closing price.

It calculates the expected % change and categorizes the stock:

Predicted % Change	Signal
> +1%	✅ BUY
-1% to +1%	🟡 HOLD
< -1%	❌ SELL / NOT BUY

Displays an easy-to-read summary with trend charts for each stock.

🛠️ Tech Stack
Purpose	Technology
Frontend Web App - Streamlit

Stock Data Source - yfinance

Machine Learning - scikit-learn

Data Processing - pandas, numpy
Visualization - matplotlib
