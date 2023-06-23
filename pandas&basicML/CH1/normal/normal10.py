### 주어진 데이터(basic2.csv)에서 "pv"컬럼으로 1일 시차(lag)가 있는 새로운 컬럼을 만들고
# (예: 1월 2일에는 1월 1일 pv데이터를 넣고, 1월 3일에는 1월 2일 pv데이터를 넣음),
# 새로운 컬럼의 1월 1일은 다음날(1월 2일)데이터로 결측치를 채운 다음, 
# Events가 1이면서 Sales가 1000000이하인 조건에 맞는 새로운 컬럼 합을 구하시오

import pandas as pd
df = pd.read_csv('../../data/basic2.csv')
df['pv_new'] = df['PV'].shift(1)
df['pv_new'] = df['pv_new'].fillna(method='bfill')

cond1 = df['Events'] == 1
cond2 = df['Sales'] <= 1000000
print(df[cond1&cond2]['pv_new'].sum())