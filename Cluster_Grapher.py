import pandas as pd
import matplotlib.pyplot as plt

path = "data/output/aniso_1000_nl_20.000000_25.000000_2.000000.csv"
df = pd.read_csv(path) 

df_clindex = df["clusterId"]
M = max(df_clindex) 
print("min, Max clusterId: ", min(df_clindex), max(df_clindex))

dfs = df["isSeed"]
print(dfs)
print("Number of seeds:", len([el for el in dfs if el == 1]))

for i in range(-1,M+1):
    dfi = df[df.clusterId == i] #i_th cluster
    plt.scatter(dfi.x0, dfi.x1, s = 5, marker = '.')

df_seed = df[df.isSeed == 1] #Only Seeds
plt.scatter(df_seed.x0, df_seed.x1, s = 20, color = 'r', marker = '*')

plt.show()
