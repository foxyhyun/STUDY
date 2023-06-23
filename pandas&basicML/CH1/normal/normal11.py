# T1-28. 시간(hour)이 13시 이전(13시 포함하지 않음) 데이터 중 
# 가장 많은 결제가 이루어진 날짜(date)는? (date 컬럼과 동일한 양식으로 출력)

import pandas as pd
df = pd.read_csv('../../data/pay.csv')

df = df[df['hour'] < 13]
print(df['date'].value_counts().index[0])