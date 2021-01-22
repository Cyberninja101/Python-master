import numpy as np
import pandas as pd
import os

x = os.walk(os.getcwd())
for i in x:
    print(i)

# df = pd.DataFrame(np.random.rand(4,3), columns=["a", "b", "c"])
# print(df)
# df= df.sample(frac=1)
# print(df)
# df.sort_index(inplace=True)
# print(df)