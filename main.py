import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("📊 SmartStock Advisor (Safe & Stable)")
st.write("Free live stock tracker that predicts **Buy / Hold / Sell** using Yahoo Finance data.")

# -------------------------------
# User Input
# -------------------------------
stocks = st.text_input("Enter stock symbols (comma-separated):", "AAPL,GOOG,MSFT,TSLA,AMZN")
stock_list = [s.strip().upper() for s in stocks.split(",")]
period = st.selectbox("Select time period:", ["1mo", "3mo", "6mo", "1y"], index=0)

if st.button("Fetch and Predict"):
    st.info("📡 Fetching live data and predicting... please wait ⏳")
    results = {}

    for stock in stock_list:
        try:
            df = yf.download(stock, period=period, interval="1d", progress=False)

            # Ensure dataframe is valid
            if df is None or df.empty:
                st.warning(f"⚠️ No data found for {stock}. Skipping.")
                continue

            # Fix for multi-level columns (sometimes returned by yfinance)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            # Ensure 'Close' column exists
            if "Close" not in df.columns:
                st.warning(f"⚠️ 'Close' column missing for {stock}. Skipping.")
                continue

            df = df.dropna(subset=["Close"])
            if len(df) < 5:
                st.warning(f"⚠️ Not enough valid data for {stock}. Skipping.")
                continue

            df["Days"] = np.arange(len(df))

            # Train regression model
            X = df[["Days"]].values
            y = df["Close"].values
            model = LinearRegression()
            model.fit(X, y)

            # Predict next day
            next_day = np.array([[len(df) + 1]])
            predicted_price = model.predict(next_day)[0]
            last_close = df["Close"].iloc[-1]
            change = ((predicted_price - last_close) / last_close) * 100

            # Decision logic
            if change > 1:
                decision, color = "✅ BUY", "green"
            elif change < -1:
                decision, color = "❌ SELL / NOT BUY", "red"
            else:
                decision, color = "🟡 HOLD", "orange"

            results[stock] = {"change": round(change, 2), "decision": decision, "color": color}

            # Plot
            fig, ax = plt.subplots()
            ax.plot(df.index, df["Close"], label="Close Price")
            ax.set_title(f"{stock} Price Trend")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error fetching {stock}: {e}")

    # Display results
    if results:
        st.subheader("📊 Predictions and Recommendations")
        for stock, info in results.items():
            st.markdown(
                f"**{stock}** → Predicted Change: **{info['change']}%** → "
                f"<span style='color:{info['color']}; font-weight:bold'>{info['decision']}</span>",
                unsafe_allow_html=True,
            )

        best_stock = max(results, key=lambda x: results[x]["change"])
        st.success(f"💡 Best BUY candidate: **{best_stock}** ({results[best_stock]['change']}%)")
