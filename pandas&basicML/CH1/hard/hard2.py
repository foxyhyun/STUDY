# 주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구해보세요

import pandas as pd
df = pd.read_csv('../../data/vaccin.csv')
df = df.groupby('country').max()
df = df.sort_values(by='ratio', ascending=False)
top10 = df['ratio'].head(10).mean()
bottom10 = df['ratio'].tail(10).mean()
print(top10 - bottom10)