## 주어진 데이터는 고혈압 환자 치료 전후의 혈압이다. 
## 해당 치료가 효과가 있는지 대응(쌍체)표본 t-검정을 진행하시오
# 귀무가설(H0): $\mu$ >= 0
# 대립가설(H1): $\mu$ < 0
# mu = (치료 후 혈압 - 치료 전 혈압)의 평균
# 유의수준: 0.05

# mu의 표본평균은?(소수 둘째자리까지 반올림)
# 검정통계량 값은?(소수 넷째자리까지 반올림)
# p-값은?(소수 넷째자리까지 반올림)
# 가설검정의 결과는? (유의수준 5%)

import pandas as pd
df = pd.read_csv('../data/high_blood.csv')

# 1.
mu = (df['bp_post'] - df['bp_pre']).mean()
print(round(mu,2))
# 2. 검정 통계량
# 대응 쌍체 표본 t , 치료가 연관이 있는지 -> relation => ttest_rel
# mu가 0보다 작으니 less , 크면 greater
import scipy.stats as ss
st, pv = ss.ttest_rel(df['bp_post'], df['bp_pre'], alternative='less')
print(round(st,4))

# 3. pvalue
print(round(pv,4))

# 4.
alpha = 0.05
if pv < alpha:
    print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
else:
    print('귀무가설을 채택합니다. 대립가설을 기각합니다.')












# # 1. mu
# mu = (df['bp_post'] - df['bp_pre']).mean()
# #print(round(mu,2))

# # 2. statistic
# import scipy.stats as ss
# from scipy.stats import ttest_1samp
# st, pv = ss.ttest_rel(df['bp_post'],df['bp_pre'],alternative='less')
# #print(round(st,4))

# # 3. pvalue
# #print(round(pv,4))

# # 4. 가설검정 결과?
# alpha = 0.05
# if pv < 0.05:
#     print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
# else:
#     print('귀무가설을 채택합니다. 대립가설을 기각합니다.')