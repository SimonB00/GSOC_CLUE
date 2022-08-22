import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sklearn.datasets as ds

data, labels = ds.make_moons(n_samples=1000, shuffle=True,noise=0.05,random_state=None)

fig, ax = plt.subplots()

colours = ('green','orange','blue','pink')
for label in range(4):
	ax.scatter(x=data[labels==label,0], 
			   y=data[labels==label,1],
			   s=40,
			   label=label)

ax.set(xlabel='X',ylabel='Y',title='Examples')
plt.show()

open_file = open('moon.csv','w')
for i in range(len(data)):
	open_file.write(str(data[i][0]) + ',' + str(data[i][1]) + ',0,1\n')
open_file.close()
