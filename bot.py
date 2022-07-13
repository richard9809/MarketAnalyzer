import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style, figure
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import yfinance as yf

style.use('ggplot')

data = yf.download(tickers='GBPUSD=X', start="2021-07-16", end="2021-07-17" ,interval='15m', progress=True)
  
#declare figure
fig = go.Figure()

#Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'GBPUSD'))

# Add titles
fig.update_layout(
    title='{yf.tickers} live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#Show
fig.show()

print(data)