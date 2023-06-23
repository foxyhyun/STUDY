import pandas as pd
df = pd.DataFrame({'Name': {0: '김딴짓', 1: '박분기', 2: '이퇴근'},
                   '수학': {0: 90, 1: 93, 2: 85},
                   '영어': {0: 92, 1: 84, 2: 86},
                   '국어': {0: 91, 1: 94, 2: 83},})

## Q. 수학, 영어, 국어 점수 중 사람과 과목에 상관없이 가장 상위 점수 5개를 모두 더하고 출력하시오.
# df2 = pd.melt(df, id_vars=['Name'])
# df2 = df2.sort_values(by='value', ascending=False).head(5)
# print(df2.sum())


# Q. 수학, 영어 점수 중 사람 과목에 관계없이 90점 이상 출력
df2 = pd.melt(df, id_vars=['Name'], value_vars=['수학','영어'])
cond1 = df2['value'] >= 90
df2 = df2[cond1]
print(df2)