import pandas as pd
df = pd.read_csv('../data/titanic.csv')

# PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0            1         0       3  ...   7.2500   NaN         S
# 1            2         1       1  ...  71.2833   C85         C
# 2            3         1       3  ...   7.9250   NaN         S
# 3            4         1       1  ...  53.1000  C123         S
# 4            5         0       3  ...   8.0500   NaN         S

# PassengerId  891 non-null    int64  
#  1   Survived     891 non-null    int64  
#  2   Pclass       891 non-null    int64  
#  3   Name         891 non-null    object 
#  4   Sex          891 non-null    object 
#  5   Age          714 non-null    float64
#  6   SibSp        891 non-null    int64  
#  7   Parch        891 non-null    int64  
#  8   Ticket       891 non-null    object 
#  9   Fare         891 non-null    float64
#  10  Cabin        204 non-null    object 
#  11  Embarked     889 non-null    object 

X = df[['Pclass','SibSp','Parch','Fare']]
y = df[['Survived']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=4234)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=6, max_features=3, n_estimators=200)
model.fit(X_train, y_train)
pred = model.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,pred))

# from sklearn.model_selection import GridSearchCV
# params = {
#     'max_depth' : [2,4,6,8],
#     'max_features' : [3,5,7,9],
#     'n_estimators' : [50,100,150,200]
# }
# grid_search = GridSearchCV(model, params, cv=5)
# grid_search.fit(X_train, y_train)
# print(grid_search.best_params_)
