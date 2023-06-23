import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')
# f2가 0인 데이터를 age를 기준으로 오름차순 정렬하고, 앞에서부터 20개의 데이터를 추출한 후, f1 결측치(최소값)를 채우기 전과
# 후의 분산 차이를 계산
df = df[df['f2'] == 0].sort_values(by='age', ascending=True)
df = df[:20]
before = df['f1'].var()
df['f1'] = df['f1'].fillna(df['f1'].min())
after=  df['f1'].var()
print(before-after)