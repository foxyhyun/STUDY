## 세 가지 다른 교육 방법(A, B, C)을 사용하여 수험생들의 성적 측정

# 귀무가설(H0): 세 그룹(A, B, C) 간의 평균 성적 차이가 없다.
# 대립가설(H1 또는 Ha): 세 그룹(A, B, C) 간의 평균 성적 차이가 있다.

### 일원배치법을 수행하여 그룹 간의 평균 성적 차이가 있는지 검정하세요 
#1. f값 (소수 둘째자리)
#2. p값 (소수 여섯째자리)
#3. 검정결과 출력

# 각 그룹의 데이터
groupA = [85, 92, 78, 88, 83, 90, 76, 84, 92, 87]
groupB = [79, 69, 84, 78, 79, 83, 79, 81, 86, 88]
groupC = [75, 68, 74, 65, 77, 72, 70, 73, 78, 75]

import pandas as pd
import scipy.stats as ss

# 3 집단 이상 => ANOVA
# 일원배치분산법 => 종속변수가 한개(성적)
from scipy.stats import f_oneway
# 1. f값
f, pv = ss.f_oneway(groupA, groupB, groupC)
print(round(f,2))

# 2. pv
print(format(pv,'.6f'))

#3.
alpha = 0.05
if pv < alpha:
    print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
else:
    print('귀무가설을 채택합니다. 대립가설을 기각합니다')










# from scipy.stats import f_oneway
# f, pv = ss.f_oneway(groupA, groupB, groupC)

# # 1. f
# print(format(f,'.2f'))

# # 2. p
# print(format(pv,'.6f'))

# # 3.
# alpha = 0.05
# if pv < alpha:
#     print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
# else:
#     print('귀무가설을 채택합니다. 대립가설을 기각합니다.')