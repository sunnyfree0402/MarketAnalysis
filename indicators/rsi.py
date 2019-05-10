import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdd
import pyEX as p

ticker = 'AMD'
timeframe = '1y'

df = p.chartDF(ticker, timeframe)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']

delta = df.y.diff().dropna()
u = delta * 0
d = u.copy()
u[delta > 0] = delta[delta > 0]
d[delta < 0] = -delta[delta < 0]
u[u.index[14-1]] = np.mean( u[:14]) 
u = u.drop(u.index[:(14-1)])
d[d.index[14-1]] = np.mean( d[:14]) 
d = d.drop(d.index[:(14-1)])
rs = pdd.stats.moments.ewma(u, com=14-1, adjust=False) / \
pdd.stats.moments.ewma(d, com=14-1, adjust=False)
rsi = 100 - 100 / (1 + rs)

plt.plot(df.ds, rsi, label='AMD RSI', color='orange')
plt.legend(loc='upper left')
plt.show()




