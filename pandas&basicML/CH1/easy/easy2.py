import pandas as pd
import numpy as np
# f5 컬럼 minmax 변환 후, 상위 5%, 하위 5% 값의 합
df = pd.read_csv('../../data/basic1.csv')
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['new'] = scaler.fit_transform(df[['f5']])
top5 = df['new'].quantile(0.05)
bottom5 = df['new'].quantile(0.95)
print(top5 + bottom5)