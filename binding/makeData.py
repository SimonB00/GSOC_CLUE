import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sklearn.datasets as ds
import random

nsamples = 100

# create vertical data
mean = 0
sigma = 0.5
z = np.random.normal(mean,sigma,100)


blob_file = open('blob_noise.csv','w')
# create blob dataset
centers = [[-10,-5],[2,4],[-10,5],[5,-7.5]]
for value in z:
	blob_data, blob_labels = make_blobs(n_samples=nsamples,centers=np.array(centers))

	for i in range(len(blob_data)):
		blob_file.write(str(blob_data[i][0]) + ',' + str(blob_data[i][1]) + ',' + str(value) + ',1\n')

n_noise = 100
for i in range(n_noise):
	x_noise = random.uniform(-15,10) 
	y_noise = random.uniform(-13,12)
	z_noise = random.uniform(-4,4)

	blob_file.write(str(x_noise) + ',' + str(y_noise) + ',' + str(z_noise) + ',1\n')

blob_file.close()

sigma = 0.1
z = np.random.normal(mean,sigma,100)
moon_file = open('moon.csv','w')
# create moon dataset
for value in z:
	moon_data, moon_labels = ds.make_moons(n_samples=150,shuffle=False,noise=0.03,random_state=None)

	for i in range(len(moon_data)):
		moon_file.write(str(moon_data[i][0]) + ',' + str(moon_data[i][1]) + ',' + str(value) + ',1\n')
moon_file.close()

sigma = 0.1
z = np.random.normal(mean,sigma,100)
circ_file = open('circles.csv','w')
# create circles dataset
for value in z:
	circ_data, circ_labels = ds.make_circles(n_samples=nsamples,shuffle=True,noise=0.0,factor=0.5)

	for i in range(len(circ_data)):
		circ_file.write(str(circ_data[i][0]) + ',' + str(circ_data[i][1]) + ',' + str(value) + ',1\n')
circ_file.close()
