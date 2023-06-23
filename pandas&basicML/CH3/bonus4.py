# p4.csv 파일에는 신약을 특정 질병 집단에 
# 투약 전후 측정한 혈류량이 저장되어 있다. 
# 이 데이터를 바탕으로 투약 전후의 변화가 있는지 
# 검정하고자 한다.

# 한 집단에 실험 연관성 파악 -> ttest_rel

import scipy.stats as ss 
st, pv = ss.ttest_rel(before, after)

# 이후 생략