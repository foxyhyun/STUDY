## 고객과 잘 맞는 타입 추천 :)
### basic1 데이터와 basic3 데이터를 'f4'값을 기준으로 병합하고, 
### 병합한 데이터에서 r2결측치를 제거한다음, 앞에서 부터 20개 데이터를 선택하고 'f2'컬럼 합을 구하시오

#- basic1.csv: 고객 데이터 
#- basic3.csv: 잘 어울리는 관계 데이터 (추천1:r1, 추천2:r2)

import pandas as pd
df1 = pd.read_csv('../../data/merge1.csv')
df2 = pd.read_csv('../../data/merge3.csv')

df = pd.merge(left=df1, right=df2, how='left', on='f4')

df.drop('r2', axis=1)
df = df[:20]
print(df['f2'].sum())