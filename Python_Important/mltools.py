from sklearn.preprocessing import LabelEncoder

def label_encoder(series):
   le = LabelEncoder().fit(series)
   return le.transform(series)

# def gen_num_data2(df):
#    num_data = df.copy()
#    for i in range(len(df.columns)):
#       if type(df.iloc[0, i]) == str:
#          num_data.iloc[:, i] = label_encoder(df.iloc[:,i])
#     return num_data


def gen_num_data(df):
   num_data = df.copy()
   for i in list(df.columns):
      if type(df.loc[0,i]) == str:
         num_data[i] = label_encoder(df[i])
   return num_data

