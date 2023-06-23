## 주어진 데이터에서 2022년 5월 주말과 평일의 sales컬럼 평균값 차이를 구하시오 (소수점 둘째자리까지 출력, 반올림)

import pandas as pd
df = pd.read_csv('../../data/basic2.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['dayofweek'] = df['Date'].dt.dayofweek

df['weekend'] = df['dayofweek'].apply(lambda x: x>=5)


cond1 = df['Year'] == 2022
cond2 = df['Month'] == 5

result1 = df[cond1&cond2&df['weekend']]['Sales'].mean()
result2 = df[cond1&cond2&~df['weekend']]['Sales'].mean()
print(result1-result2)