import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')

# age 컬럼 상위 20개의 데이터를 구한다음, f1 결측치를 중앙값으로 채운다.
# f4가 ISFJ와 f5가 20 이상인 f1 평균값 출력
df = df.sort_values(by='age', ascending=False)
df = df[:20]
df['f1'] = df['f1'].fillna(df['f1'].median())
print(df[(df['f4'] == 'ISFJ')&(df['f5']>=20)]['f1'].mean())