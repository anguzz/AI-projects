

from math import *
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn import neighbors
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("data.csv")
ans = pd.read_csv("test.csv")
X = dataset.drop("Weight", axis=1)
y = dataset["Weight"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rmse = [] 

for K in range(5):
    K = K+1
    m = neighbors.KNeighborsRegressor(n_neighbors=K)
    m.fit(X_train, y_train) #model fit
    pred = m.predict(X_test) # predict test set
    err = sqrt(mean_squared_error(y_test, pred)) # calculate rmse
    rmse.append(err) # store rmse 
   
   

print("Predicted weights in order are ")
m = neighbors.KNeighborsRegressor(n_neighbors=4)
m.fit(X, y) 
pred = m.predict(ans) 
print(pred)