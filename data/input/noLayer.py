from hashlib import new
import pandas as pd

path = ""
df = pd.read_csv("sissa_4000.csv")
print(df)
new_df = pd.concat([df['x0'],df['x1'],df['weight']],axis=1)
print(new_df)

len_ = len(new_df['x0'].values.tolist())

with open("sissa_4000.csv","w") as file:
    for i in range(len_):
        file.write(str(new_df['x0'][i]) + ',' + str(new_df['x1'][i]) + ',' + str(new_df['weight'][i]) + '\n')
