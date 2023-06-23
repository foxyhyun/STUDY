
# 평균키는 165cm라 판단할 수 있는지 
# 귀무가설과 대립가설을 설정한 후 유의수준 5%로 
# 검정하고자 한다.


# 데이터 x 

# 단순 한 집단의 평균 검정이므로 -> ttest_1samp
import scipy.stats as ss 
mu = 165
# alternative도 없음
st, pv = ss.ttest_1samp(data, mu)

# 이후 생략