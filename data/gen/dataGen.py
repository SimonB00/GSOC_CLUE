import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mean0 = 0
sigma0 = 50
x0 = np.random.normal(mean0,sigma0,1000)
mean1 = 0
sigma1 = 60
x1 = np.random.normal(mean1,sigma1,1000)
mean2 = 0
sigma2 = 80
x2 = np.random.normal(mean2,sigma2,1000)

x0 = list(x0)
x1 = list(x1)
x2 = list(x2)
print(type(x0))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x0,x1,x2)
plt.show()

open_file = open("gen.csv", 'w')
for i in range(len(x0)):
    open_file.write(str(round(x0[i],2)) + ',' + str(round(x1[i],2)) + ',' + str(round(x2[i],2)) + ',0.00,1.00' + '\n')
