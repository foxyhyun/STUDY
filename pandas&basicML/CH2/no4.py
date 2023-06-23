import pandas as pd
import numpy as np
df = pd.read_csv('../data/housePrice.csv')

df = df.select_dtypes(exclude=['object'])

X = df.iloc[:,:-1]
y = df['SalePrice']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=4234)

from sklearn.impute import SimpleImputer
scaler = SimpleImputer()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

from sklearn.ensemble import RandomForestRegressor
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)
pred_rf = model_rf.predict(X_test)
from sklearn.metrics import mean_squared_error


def rmse(y_test, pred):
    return np.sqrt(mean_squared_error(y_test, pred))

print(rmse(y_test, pred_rf))

from xgboost import XGBRegressor
model_xgb = XGBRegressor()
model_xgb.fit(X_train, y_train)
pred_xgb = model_xgb.predict(X_test)
print(rmse(y_test, pred_xgb))