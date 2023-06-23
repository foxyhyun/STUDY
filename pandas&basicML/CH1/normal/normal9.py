## 나이 구간 나누기
###  basic1 데이터 중 'age'컬럼 이상치를 제거하고, 동일한 개수로 나이 순으로 3그룹으로 나눈 뒤 각 그룹의 중앙값을 더하시오
### (이상치는 음수(0포함), 소수점 값)

import pandas as pd
import numpy as np
df = pd.read_csv('/Users/foxyhyun/Desktop/bigdataCertificate/data/basic1.csv')

outlier1 = df['age'] > 0
outlier2 = (df['age'] - np.floor(df['age']) == 0)

df2 = df[outlier1&outlier2]
df['range'] = pd.qcut(df2['age'], q=3, labels={'g1','g2','g3'})
q1 =df[df['range'] == 'g1']['age'].median()
q2 =df[df['range'] == 'g2']['age'].median()
q3 =df[df['range'] == 'g3']['age'].median()
print(q1+q2+q3)