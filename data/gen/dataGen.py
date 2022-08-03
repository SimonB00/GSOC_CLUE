import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mean = [0, 0, 0]
cov = [[2,0,0], [0,2,0], [0,0,2]]
x0, x1, x2 = np.random.multivariate_normal(mean, cov, 100000).T

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
    open_file.write(str(i) + ',' + str(x0[i]) + ',' + str(x1[i]) + ',' + str(x2[i]) + ',0,1' + '\n')