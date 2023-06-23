import pandas as pd
import numpy as np
df = pd.read_csv('../data/adult.csv')






# ========전처리 시작 ============
# 결측치 처리 -> isnull.sum으로 확인 불가 => ? 로 표시되어 있음
df[df=='?'] = np.nan
for col in ['workclass','occupation','native.country']:
    df[col].fillna(df[col].mode()[0], inplace=True)
    
# X,y 지정
X = df.drop(['income','education','fnlwgt'], axis=1)
y = df['income']

# all_df to train, val data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4234)

# 범주형 숫자로 변환
from sklearn.preprocessing import LabelEncoder
cat_col = ['workclass','marital.status','occupation','relationship','race','sex','native.country']
for col in cat_col:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col]) # train => fit_transform
    X_test[col] = le.transform(X_test[col]) # test => transform
    
# 수치형 스케일링
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

# 타깃값 => 0,1로 변경
y_train = (y_train=='<=50K').astype(int)
y_test = (y_test=='<=50K').astype(int)

# =========전처리끝========

# ======모델시작=====
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)
pred = model.predict(X_test_scaled)

# 모델 평가
# 1.
# from sklearn.metrics import classification_report
# print(classification_report(y_test, pred))

# # 2. 
# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(y_test, pred))

# 모델 개선
from sklearn.model_selection import GridSearchCV
#print(help(GridSearchCV))
#print(help(RandomForestClassifier))
params = {
    # rfc help쳐서 파라미터 작성
    'n_estimators':[50,100,150,200],
    'max_depth':[3,6,9,12],
    'max_features':[2,4,6,8]
}
# grid_search = GridSearchCV(model, params, cv=5)
# grid_search.fit(X_train_scaled, y_train)
# print(grid_search.best_params_)
# => 위의 결과{'max_depth': 12, 'max_features': 6, 'n_estimators': 200}

final_model = RandomForestClassifier(max_depth=12, max_features=6, n_estimators= 200)
final_model.fit(X_train_scaled, y_train)
pred = final_model.predict(X_test_scaled)

from sklearn.metrics import classification_report
#print(classification_report(y_test, pred))
# 0.82에서 0.86으로 성능 개선
