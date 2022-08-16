import pandas as pd
import matplotlib.pyplot as plt

def count_el(l, el):
    counts = 0
    for i in l:
        if i == el:
            counts += 1
    return counts

path = "data/output/aniso_1000_nl_20.000000_25.000000_2.000000.csv"
df = pd.read_csv(path) #Produces a DataFrame type

df_clindex = df["clusterId"] #SERIES of clusterId
M = max(df_clindex) #max cluster index (i.e. number of clusters starting from 0)
print("min, Max clusterId: ", min(df_clindex), max(df_clindex))

dfs = df["isSeed"]
print(dfs)
print("Number of seeds:", count_el(dfs, 1))

for i in range(-1,M+1):
    dfi = df[df.clusterId == i] #i_th cluster
    #print(dfi)
    plt.scatter(dfi.x0, dfi.x1, s = 5, marker = '.')

df_seed = df[df.isSeed == 1] #Only Seeds
plt.scatter(df_seed.x0, df_seed.x1, s = 20, color = 'r', marker = '*')

plt.show()
