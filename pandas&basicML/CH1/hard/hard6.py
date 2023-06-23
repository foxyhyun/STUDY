
# 12월 25일 결제 금액(price)은 12월 총 결제금액의 몇 %인가? (정수로 출력)

import pandas as pd
df = pd.read_csv("../../data/pay.csv")

df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df
