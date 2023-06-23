

# 모르겠으면 그냥 
# import scipy.stats
# print(help(scipy.stats))

# 한 집단의 평균 검정 -> ttest_1samp(비교 컬럼1, 비교컬럼2, alternative)
# 한 집단에서의 실험의 연관성 검정 -> ttest_rel(data, mu, alternative
# 두 집단에서의 평균 차이 검정 -> ttest_ind(group1, group2)
# 집단 3개 이상? => ANOVA 
# 일원배치분산법 => f1_oneway(group1, group2, group3, .....)
# 정규성 분포 가정판단 => shapiro 검정 : shapiro(data)

# 집단간 비교는 오히려 간단하다. 함수 옆에 파라미터에 그룹만 적어주면 끝