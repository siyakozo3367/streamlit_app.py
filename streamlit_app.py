from datetime import datetime, timedelta
import pytz
import streamlit as st

# South Africa timezone
sast = pytz.timezone("Africa/Johannesburg")

# Get current time and expiry time
now = datetime.now(sast)
expiry = now + timedelta(minutes=1)

# Format times
now_str = now.strftime("%H:%M:%S")
expiry_str = expiry.strftime("%H:%M:%S")

# Streamlit UI
st.title("Pocket Option Signal Bot")
st.header("Live Signals")

# Example signals
st.write(f"{now_str} — AED/CNY: Sell Signal (72%) — Expiry: {expiry_str}")
st.write(f"{now_str} — AUD/CHF: Sell Signal (80%) — Expiry: {expiry_str}")

st.write("Strategy: AI Trend Reversal")
