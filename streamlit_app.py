import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import pytz

# Set timezone
sast = pytz.timezone("Africa/Johannesburg")
now = datetime.now(sast)
expiry = now + timedelta(minutes=1)

# Trading pairs and their Yahoo tickers
symbols = {
    "AED/CNY": "CNY=X",     # Approx proxy
    "AUD/CHF": "AUDCHF=X",
    "USD/JPY": "USDJPY=X",
}

# Strategy function: AI Trend Reversal
# Uses RSI and EMA to decide Buy/Sell
import ta

def get_signal(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['ema'] = ta.trend.EMAIndicator(df['Close']).ema_indicator()

    latest = df.iloc[-1]
    if latest['rsi'] < 30 and latest['Close'] > latest['ema']:
        return "Buy"
    elif latest['rsi'] > 70 and latest['Close'] < latest['ema']:
        return "Sell"
    else:
        return "Hold"

# Streamlit UI
st.title("Pocket Option Signal Bot")
st.caption("Live Trading Signals — Updated Every 60s")
st.markdown(f"**Time (SAST):** {now.strftime('%H:%M:%S')} | **Expiry:** {expiry.strftime('%H:%M:%S')}")

# Generate and display signals
for name, ticker in symbols.items():
    try:
        data = yf.download(ticker, period="1d", interval="1m")
        if not data.empty:
            signal = get_signal(data)
            st.success(f"{name}: {signal} Signal")
        else:
            st.warning(f"{name}: No data available")
    except Exception as e:
        st.error(f"{name}: Error fetching data")

# Auto-refresh every 60s
st.experimental_rerun()
