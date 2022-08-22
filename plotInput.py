import matplotlib.pyplot as plt
import pandas as pd

file = input('What file do you want to plot? ')
Ndim = int(input('Number of dimensions? '))

df = pd.read_csv(file,header=None)
len_ = len(df[0].values.tolist())

data = []
for i in range(Ndim):
	data.append([])

for i in range(len_):
	for j in range(Ndim):
		data[j].append(df[j][i])

plt.scatter(x=data[0],y=data[1],s=1)
plt.show()
