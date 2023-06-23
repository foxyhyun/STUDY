# 다이어트약의 체중 감량 효과를 실험하기 위해 정해진 기간 복용 후 
# 체중을 측정하였다.
before=[60,65,70,75,80] 
# 다이어트약 복용 전 체중 
after=[58,62,68,72,78] 
# 다이어트약 복용 후 체중
# 대응표본 t-검정을 통해 체중 변화가 유의미하게 있는지 확인하려고 한다.

# 한 집단 실험 연관성 검정 -> ttest_rel
import scipy.stats as ss 
st, pv = ss.ttest_rel(before, after)
print(st)
print(pv)