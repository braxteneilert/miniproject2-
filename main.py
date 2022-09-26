# INF601 - Advanced Programming in Python
# Braxten Eilert
# Mini Project 1



import yfinance as yf
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import requests

df = yf.download('SPY', start='2019-01-01')


df['MA200'] = df['Adj Close'].rolling(200).mean()
df['MA100'] = df['Adj Close'].rolling(100).mean()
df = df[['Adj Close', 'MA100', 'MA200']]
#df.to_excel('SPY.xlsx')
print(df)
plt.plot(df['Adj Close'], label= 'price', c='blue', alpha=0.5 )
plt.plot(df['MA200'], label='MA200', c='k', alpha=0.9)
plt.plot(df['MA100'], label='MA100', c='magenta', alpha=0.9)
plt.savefig('Charts/SPY.png')
plt.show()





