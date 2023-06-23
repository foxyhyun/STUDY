# f1의 결측치를 채운 후 age 컬럼의 중복 제거 전과 후의 'f1' 중앙값 차이를 구하시오
# 결측치는 f1의 데이터 중 내림차순 정렬 후 10번째 값으로 채움
# 중복 데이터 발생시 뒤에 나오는 데이터를 삭제함
# 최종 결과값은 절대값으로 출력

import pandas as pd
df = pd.read_csv('../../data/basic1.csv')

top10 = df['f1'].sort_values(ascending=False).iloc[9]
df['f1'] = df['f1'].fillna(top10)

before_df = df['age'].median()
df = df.drop_duplicates(subset=['age'])
after_df = df['age'].median()
print(abs(before_df - after_df))