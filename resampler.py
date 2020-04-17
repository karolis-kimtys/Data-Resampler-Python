#Python code to resample currency tick data to 1H time interval data.
#Data has to be in YYYY.MM.DD format and time has to be in HH:MM:SS format.
#Uses .CSV file

import pandas as pd
import time
from scipy.signal import argrelextrema

start_time = time.time()

df = pd.read_csv("EURCHF.csv",
            parse_dates={'DateTime': ['Date', 'Time']},
            usecols=['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'],
            na_values=['nan']).set_index('DateTime')

ohlc_dict = {'Open':'first', 'High':'max', 'Low':'min', 'Close': 'last', 'Volume': 'sum'}
df = df.resample('1H', how=ohlc_dict).dropna(how='any')

#df.iloc[0] = df.iloc[0].shift(periods=5).fillna('0')

print(df.iloc[0])

cols=['Open', 'High', 'Low', 'Close', 'Volume']
df = df[cols]

print(df.head())

df.to_csv("sampled_data.csv")

end = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
