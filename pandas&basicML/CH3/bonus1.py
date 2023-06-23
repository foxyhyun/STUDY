#아래의 데이터는 11명 학생들의 수학 점수를 모아둔 리스트이다.
data = [ 75, 82, 80, 76, 84, 81, 79, 80, 78, 83, 74 ]
#모집단의 평균값이 80일 때 일표본 t-검정(one-sample t-test)을 
# 시행하여 평균값이 유의한지 확인하려 한다.

import scipy.stats as ss 
mu = 80
# alternative는 따로 없음
st, pv = ss.ttest_1samp(data, mu)
print(st)
print(pv)
if pv< 0.05:
    print('귀무가설 기각. 대립가설 채택')
else:
    print('귀무가설 채택. 대립가설 기각')