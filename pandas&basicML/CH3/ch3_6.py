## 12명의 수험생이 빅데이터 분석기사 시험에서 받은 점수이다. 
## Shapiro-Wilk 검정을 사용하여 데이터가 정규 분포를 따르는지 검증하시오

# 귀무 가설(H0): 데이터는 정규 분포를 따른다.
# 대립 가설(H1): 데이터는 정규 분포를 따르지 않는다.

# Shapiro-Wilk 검정 통계량, p-value, 검증결과를 출력하시오**

import scipy.stats as ss
from scipy.stats import shapiro

data = [75, 83, 81, 92, 68, 77, 78, 80, 85, 95, 79, 89]

# 정규분포 따르는지 검정하라 => 샤피로 검정
# print(help(shapiro))
# shapiro_test = stats.shapiro(x)
st, pv = ss.shapiro(data)
# 1. 
print(st)
# 2.
print(pv)
# 3. 
alpha = 0.05
if pv < alpha:
    print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
else:
    print('귀무가설을 채택합니다. 대립가설을 기각합니다')
# 귀무가설 채택이므로 정규 분포 만족함







# s, pv = ss.shapiro(data)

# # 1. 
# print(s)

# # 2.
# print(pv)

# # 3.
# alpha = 0.05
# if pv < alpha:
#     print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
# else:
#     print('귀무가설을 채택합니다. 대립가설을 기각합니다.')