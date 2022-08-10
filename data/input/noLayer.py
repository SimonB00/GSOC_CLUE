from hashlib import new
import pandas as pd

path = ""
df = pd.read_csv("../gen/gen.csv")
print(df)
new_df = pd.concat([df['x'],df['y'],df['z'],df['weight']],axis=1)
print(new_df)

len_ = len(new_df['x'].values.tolist())

with open("../gen/gen_nl.csv","w") as file:
    for i in range(len_):
        file.write(str(new_df['x'][i]) + ',' + str(new_df['y'][i]) + ',' + str(new_df['z'][i]) + ',' + str(new_df['weight'][i]) + '\n')