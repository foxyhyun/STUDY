import pandas as pd
import numpy as np
df = pd.read_csv('../../data/basic1.csv')

# f5컬럼을 z 표준화하고 중앙값을 구하라
import scipy.stats as ss 
df['f5'] = ss.zscore(df['f5'])
print(df['f5'].median())