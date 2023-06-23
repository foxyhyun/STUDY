
# 주어진 데이터 중 basic1.csv에서 'f1'컬럼 결측 데이터를 제거하고, 'city'와 'f2'을 기준으로 묶어 합계를 구하고, 
# 'city가 경기이면서 f2가 0'인 조건에 만족하는 f1 값을 구하시오

import pandas as pd
df = pd.read_csv('../../data/basic1.csv')
df = df[~df.isnull()]
df2 = df.groupby(['city','f2']).sum()
print(df2.iloc[0]['f1'])