import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

pd.set_option('display.max_rows', None, 'display.max_columns', None)

file = r'/Users/zenchangsun/Downloads/cereal.csv'
data = pd.read_csv(file)
# print(data.head().to_string())
columns = list(data.columns)
columns.pop()

# print(columns)


data_num = data.copy()
# encoder = LabelEncoder()
# encoder.fit(data['type'])
# encodings = encoder.transform(data['type'])

# data_num['type'] = encoder.transform(data['type'])

def replace_num(data, column):
    encoder = LabelEncoder()
    encoder.fit(data[column])
    data[column] = encoder.transform(data[column])
    return data


for i in data.columns:
    if type(data.loc[0, i]) == str:
        data_num = replace_num(data_num, i)

X = data_num[columns]
Y = data_num['rating']

# For regression model
rgr = svm.SVR()
rgr.fit(X, Y)

split = int(len(data_num) * 0.8)

XTrain = X.iloc[0:split,1:]
XValid = X.iloc[split:,1:]
YTrain = Y.iloc[0:split]
YValid = Y.iloc[split:]
YValid = list(YValid)
print(len(XTrain), len(XValid), len(YTrain), len(YValid))

rgr.fit(XTrain, YTrain)
predictions = rgr.predict(XValid)
# print(predictions)
# print(YValid)
def absoluteError(Y_pred, Y_true):
	return  np.mean(abs(Y_pred - Y_true))
	# abs_Error = []
	# for i in range(0, len(Y_pred)):
	#     x = abs(Y_pred[i]-Y_true[i])
	#     abs_Error.append(x)
	# return np.mean(abs_Error)

def MSE(Y_pred, Y_true): 
    return sum(((Y_pred - Y_true) ** 2)/len(Y_true))

def RMSE(MSE): 
    return MSE ** 0.5

print("The Absolute Error is: " + str(absoluteError(predictions, YValid)))

print(rgr.score(XValid, YValid))



rgr2 = DecisionTreeRegressor()
rgr2.fit(XTrain, YTrain)
predictions2 = rgr2.predict(XValid)
print("The Absolute Error is: " + str(absoluteError(predictions2, YValid)))
print(rgr2.score(XValid, YValid))
print("Test MSE function")
print(RMSE(MSE(predictions2, YValid)))



