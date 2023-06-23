import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')
# f4가 E로 시작하면서 부산에 살고 20대인 사람은 몇명?
cond1 = df['f4'].str[0] == 'E'
cond2 = df['city'] == '부산'
cond3 = (df['age']>=20)&(df['age']<30)
print(len(df[cond1&cond2&cond3]))