import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sklearn.datasets as ds

nsamples = 100

# create vertical data
mean = 0
sigma = 0.5
z = np.random.normal(mean,sigma,100)


blob_file = open('blob.csv','w')
# create blob dataset
centers = [[-10,-5],[2,4],[-10,5],[5,-7.5]]
for value in z:
	blob_data, blob_labels = make_blobs(n_samples=nsamples,centers=np.array(centers))

	for i in range(len(blob_data)):
		blob_file.write(str(blob_data[i][0]) + ',' + str(blob_data[i][1]) + ',' + str(value) + ',1\n')
blob_file.close()

sigma = 0.1
z = np.random.normal(mean,sigma,100)
moon_file = open('moon.csv','w')
# create moon dataset
for value in z:
	moon_data, moon_labels = ds.make_moons(n_samples=nsamples, shuffle=True,noise=0.05,random_state=None)

	for i in range(len(moon_data)):
		moon_file.write(str(moon_data[i][0]) + ',' + str(moon_data[i][1]) + ',' + str(value) + ',1\n')
moon_file.close()
