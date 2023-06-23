# 한 기계 부품의 rpm 수치를 두 가지 상황에서 
# 측정하고 p10.csv에 저장하였다. 
# b 상황이 a 상황보다 rpm 값이 높다고
# 할 수 있는지 검정하려 한다.

# 연관성 검정 -> ttest_rel
# 대립가설 : a > b

import scipy.stats as ss 
st, pv = ss.ttest_rel(b,a, alternative='greater')

# 이후 생략