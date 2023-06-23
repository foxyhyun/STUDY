# 주어진 데이터(basic2.csv)에서 주 단위 Sales의 합계를 구하고, 가장 큰 값을 가진 주와 작은 값을 가진 주의 차이를 구하시오(절대값)

import pandas as pd
df = pd.read_csv('../../data/basic2.csv', parse_dates=['Date'],index_col=0)

df_w = df.resample('W').sum()
max = df_w['Sales'].max()
min = df_w['Sales'].min()
print(abs(max-min))