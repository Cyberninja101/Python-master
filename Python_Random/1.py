
import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.rand(50,3), columns=[ "a", "b", "c"])
#print(df)

split_col = "a"
split = df.loc[0,split_col]

right = df.loc[df[split_col] > split]
left = df.loc[df[split_col] <= split]

y_true = list(df["c"])
right["c"] = np.mean(right["c"])
left["c"] = np.mean(left['c'])
y_pred = list(pd.concat([right["c"], left["c"]]).sort_index())

print(df)
print(right)
print(left)

print(y_pred)
print(y_true)
