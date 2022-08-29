import pandas as pd
import matplotlib.pyplot as plt
import glob

def getFolder(file):
	reversed = file[::-1]

	folder = ''
	begin = False
	for char in reversed:
		if char == '/':
			begin = True
		if begin:
			folder += char
	
	return folder[::-1]

fileNotFound = True
file = ''

while fileNotFound:
	file = input('What file do you want to plot? ')

	folder = getFolder(file) + '*'
	files = glob.glob(folder)
	if file in files:
		fileNotFound = False
	else:
		print('File not found')

df = pd.read_csv(file) 
Ndim = len(df.columns) - 1

df_clindex = df["clusterId"]
M = max(df_clindex) 
print("min, Max clusterId: ", min(df_clindex), max(df_clindex))

dfs = df["isSeed"]
print("Number of seeds:", len([el for el in dfs if el == 1]))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

df_outl = df[df.clusterId == -1]
ax.scatter(df_outl.x0, df_outl.x1, df_outl.x2, s=15, color = 'grey', marker = 'x')
for i in range(0,M+1):
    dfi = df[df.clusterId == i] #i_th cluster
    ax.scatter(dfi.x0, dfi.x1, dfi.x2, s = 5, marker = '.')

df_seed = df[df.isSeed == 1] #Only Seeds
ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s = 20, color = 'r', marker = '*')

plt.show()
