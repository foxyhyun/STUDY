# 왜도와 첨도 구하기
# age 컬럼 왜도와 첨도 구하기
# 이후 age 컬럼 log1p 변환 후 왜도와 첨도 구해서 위에꺼랑 더해서 출력
import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')

skew = df['age'].skew()
kurt = df['age'].kurt()

df['age'] = np.log1p(df['age'])
skew2 = df['age'].skew()
kurt2 = df['age'].kurt()

print(skew+skew2+kurt+kurt2)