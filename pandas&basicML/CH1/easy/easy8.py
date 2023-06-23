import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic2.csv')
# 2022년 5월 sales의 중앙값
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
cond1 = df['Year'] == 2022
cond2 = df['Month'] == 5
print(df[cond1&cond2]['Sales'].median())