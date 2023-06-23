## 어떤 특정 약물을 복용한 사람들의 평균 체온이 
## 복용하지 않은 사람들의 평균 체온과 유의미하게 다른지 검정

#가정:
# 약물을 복용한 그룹과 복용하지 않은 그룹의 체온 데이터가 각각 주어져 있다고 가정합니다.
# 각 그룹의 체온은 정규분포를 따른다고 가정합니다.

## 검정통계량, p-value, 검정결과를 출력하시오

# 데이터 수집
group1 = [36.8, 36.7, 37.1, 36.9, 37.2, 36.8, 36.9, 37.1, 36.7, 37.1]
group2 = [36.5, 36.6, 36.3, 36.6, 36.9, 36.7, 36.7, 36.8, 36.5, 36.7]


# 그룹이 2개 => ttest_ind
# 1. 검정통계량
import scipy.stats as ss 
st, pv = ss.ttest_ind(group1, group2)
print(st)

# 2. pvalue
print(pv)

# 3. result
alpha = 0.05
if pv < alpha:
    print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
else:
    print('귀무가설을 채택합니다. 대립가설을 기각합니다')












# import pandas as pd
# import scipy.stats as ss
# from scipy.stats import ttest_ind

# st, pv = ss.ttest_ind(group1, group2)

# 1.
#print(round(st,4))

# 2.
# print(round(pv,4))

# 3.
# alpha = 0.05
# if pv < alpha:
#     print('귀무가설을 기각합니다. 대립가설을 채택합니다.')
# else:
#     print('귀무가설을 채택합니다. 대립가설을 기각합니다.')