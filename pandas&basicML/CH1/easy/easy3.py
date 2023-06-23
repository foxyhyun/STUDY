import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')
# f4 컬럼이 ENFJ인 컬럼과 INFP인 컬럼의 f1 값의 표준편차 차이 절대값으로 표현
enfj = df[df['f4'] == 'ENFJ']['f1'].std()
infp = df[df['f4'] == 'INFP']['f1'].std()
print(abs(enfj-infp))