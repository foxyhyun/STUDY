
# Q. 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고, 
# 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력

import pandas as pd
df = pd.read_csv('../../data/basic1.csv')
#print(df.head(5))

#print((df.isnull().sum())/df.shape[0]*100)
df = df.drop('f3', axis=1)
#print(df['city'].value_counts())

k = df[df['city'] == '경기']['f1'].median()
s = df[df['city'] == '서울']['f1'].median()
d = df[df['city'] == '대구']['f1'].median()
b = df[df['city'] == '부산']['f1'].median()

df['f1'] = df['f1'].fillna(df['city'].map({
    '경기':k,
    '서울':s,
    '대구':d,
    '부산':b
}))

print(df.head())

