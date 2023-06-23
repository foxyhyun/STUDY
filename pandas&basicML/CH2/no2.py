import pandas as pd
df = pd.read_csv('../data/diabetes.csv')

col = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
df[col] = df[col].replace(0,df[col].mean())


X = df.iloc[:,:-1]
y = df['Outcome']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=4234)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
pred = model.predict(X_test)
from sklearn.metrics import classification_report
#print(classification_report(y_test, pred))
# accuracy -> 0.77

# from sklearn.model_selection import GridSearchCV
# params = {
#     'max_depth':[3,5,7,9],
#     'max_features':[2,4,6,8],
#     'n_estimators':[50,100,150,200]
# }
# grid_search = GridSearchCV(model, params, cv=5)
# grid_search.fit(X_train, y_train)
# print(grid_search.best_params_)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=5, max_features=2, n_estimators=100)
model.fit(X_train, y_train)
pred = model.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, pred))
# 0.76 => f1값 비교할것!