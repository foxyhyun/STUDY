# 주어진 데이터에서 2022년 월별 Sales 합계 중 
# 가장 큰 금액과 2023년 월별 Sales 합계 중 가장 큰 금액의 차이를 절대값으로 구하시오.
# 단 Events컬럼이 '1'인경우 80%의 Salse값만 반영함 (최종값은 소수점 반올림 후 정수 출력)

import pandas as pd
df = pd.read_csv('../../data/basic2.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

def Events(df):
    if df['Events'] == 1:
        df['Sales'] = df['Sales']*0.8
    return df

df = df.apply(lambda x : Events(x), axis=1)

df2022 = df['Year'] == 2022
df2023 = df['Year'] == 2023
df2022 = df[df2022].groupby('Month')['Sales'].sum().max()
df2023 = df[df2023].groupby('Month')['Sales'].sum().max()

print(abs(df2022 - df2023))