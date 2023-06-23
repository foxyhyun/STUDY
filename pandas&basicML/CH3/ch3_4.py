import pandas as pd
from sklearn.datasets import load_iris

# iris 데이터셋 로드
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Sepal Length와 Sepal Width 상관계수 구하기
corr = df.corr()
print(corr)
print(corr.iloc[1][0]) # 이건 그냥 corr 결과보고 iloc으로 위치 찾기














# ## iris에서 Sepal Length와 Sepal Width의 상관계수 계산하고 소수 둘째자리까지 출력하시오
# print(df.head())
# corr = df.corr()
# result = corr.loc['sepal length (cm)','sepal width (cm)']
# print(round(result,2))