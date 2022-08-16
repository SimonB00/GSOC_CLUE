from hashlib import new
import pandas as pd

path = ""
df = pd.read_csv("toyDetector_1000.csv")
print(df)
new_df = pd.concat([df['x'],df['y'],df['weight']],axis=1)
print(new_df)

len_ = len(new_df['x'].values.tolist())

with open("toyDetector_1000_nl.csv","w") as file:
    for i in range(len_):
        file.write(str(new_df['x'][i]) + ',' + str(new_df['y'][i]) + ',' + str(new_df['weight'][i]) + '\n')
