#p3.csv 파일에는 A, B 두 학급 각 학생들의 중간고사 평균 
# 점수들이 저장되어 있다.
#두 학급의 시험 평균(비모수검정의 경우 중위값)은 
# 동일하다 말할 수 있는지 확인하려 한다.

# 2 그룹간의 평균 비교 -> ttest_ind
import scipy.stats as ss 
st, pv = ss.ttest_ind(groupA, groupB)

# 이후 생략