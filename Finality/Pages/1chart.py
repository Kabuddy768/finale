import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def add_technical_indicator(fig, df, indicators):
    for indicator in indicators:
        if indicator == 'MA':
            fig.add_trace(go.Scatter(x=df.index, y=ma_50, mode='lines', name='50-day MA', line=dict(color='black')))
        elif indicator == 'RSI':
            fig.add_trace(go.Scatter(x=df.index, y=rsi, mode='lines', name='RSI', line=dict(color='blue')))
        elif indicator == 'BB':
            fig.add_trace(go.Scatter(x=df.index, y=upper_band, mode='lines', name='Upper Bollinger Band', line=dict(color='purple')))
            fig.add_trace(go.Scatter(x=df.index, y=lower_band, mode='lines', name='Lower Bollinger Band', line=dict(color='purple')))

# Dowload AAPL data
symbol = "KES=X"
start_date = "2020-01-01"
end_date = "2024-03-30"
df = yf.download(symbol, start=start_date, end=end_date)

# Calculate 50-day moving average
ma_50 = df['Close'].rolling(window=50).mean()

# Calculate RSI
delta = df["Close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

# Calculate Bollinger Bands
rolling_mean = df["Close"].rolling(window=20).mean()
rolling_std = df["Close"].rolling(window=20).std()
upper_band = rolling_mean + (2 * rolling_std)
lower_band = rolling_mean - (2 * rolling_std)

# Define available indicators
available_indicators = ['MA', 'RSI', 'BB']

# Initialize selected indicators
selected_indicators = []

# Checkbox loop
for indi in available_indicators:
    checked = st.checkbox(indi, key=indi)
    if checked:
        selected_indicators.append(indi)

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Add selected technical indicators to the chart
add_technical_indicator(fig, df, selected_indicators)

# Customize the chart layout
fig.update_layout(title="{} Stock Price with Selected Technical Indicators".format(symbol),
                  xaxis_title="Date",
                  yaxis_title="Price")

# Display the chart
st.plotly_chart(fig)