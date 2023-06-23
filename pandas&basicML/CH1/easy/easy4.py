# f4 컬럼의 값이 ESFJ인 데이터를 ISFJ로 대체하고, city가 경기이면서 f4가 ISFJ인 데이터 중 age 컬럼의 최대값
import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')

df['f4'] = df['f4'].replace('ESFJ','ISFJ')
print(df[(df['city'] == '경기')&(df['f4']=='ISFJ')]['age'].max())