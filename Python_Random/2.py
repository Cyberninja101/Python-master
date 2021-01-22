# default decision tree split pseudo code
for j in features:
    for i in rows:
        SPLIT(i,j)

# default decision tree split python ish
for j in df.columns:
    for i in df[j]:
        #Split
        value = df.loc[i,j]
        left = df.loc[df[j] < value]
        right = df.loc[df[j] >= value]

# default decision tree split  random feature
j = np.choice(df.columns)
for i in df[j]:
    SPLIT(i,j)

# default decision tree split random row
for j in features:
    i = np.choice(df[j])
    SPLIT(i,j)

# default decision tree split random row and feature
j = np.choice(df.columns)
i = np.choice(df[j])
SPLIT(i,j)

class decision_tree():

    def __init__(self, min_sample_leaf=1, max_depth=None, max_feature=None):
        self.min_sample_leaf = min_sample_leaf
        self.max_depth = max_depth
        self.max_feature = max_feature

    def split(df, y_train):
        mse_array = np.ones(df.size) * 1e9
        for j in df.columns:
            for i in df[j]:
                #Split
                value = df.loc[i,j]
                left = df.loc[df[j] < value]
                right = df.loc[df[j] >= value]
                y_pred_left = mean(y_train.loc[left.index])
                y_pred_right = mean(y_train.loc[right.index])
                indexes = list(left.index) + list(right.index)
                indexes.sort_index(inplace=True)
                

                y_pred_left = np.ones(len(left)) * y_pred_left
                y_pred_right = np.ones(len(right)) * y_pred_right
                y_pred = y_pred_left.append(y_pred_right)
                y_pred = pandas.Series(y_pred)
                y_pred.set_index(indexes,inplace=True)
                y_pred.sort_index(inplace=True)

                mse = get_mse(y_train, y_pred)
        return left, right, i, j
 




    def fit(X, y):
        split(X)


    return results of test