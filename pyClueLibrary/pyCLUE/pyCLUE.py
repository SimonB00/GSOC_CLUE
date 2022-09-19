import pandas as pd
import numpy as np
import random as rnd
import time
import matplotlib.pyplot as plt
import clusteringAlgo as Algo 
from sklearn.datasets import make_blobs

def sign():
	sign = rnd.random()
	if sign > 0.5:
		return 1
	else:
		return -1

def makeBlobs(nSamples, Ndim, nBlobs=4, mean=0, sigma=0.5):
	"""
	Returns a test dataframe containing randomly generated 2-dimensional or 3-dimensional blobs. 

	Parameters:
	nSamples (int): The number
	Ndim (int): The number of dimensions.
	nBlobs (int): The number of blobs that should be produced. By default it is set to 4.
	mean (float): The mean of the gaussian distribution of the z values.
	sigma (float): The standard deviation of the gaussian distribution of the z values.
	"""

	if Ndim == 2:
		data = {'x0': [], 'x1': [], 'weight': []}
		blob_data, blob_labels = make_blobs(n_samples=nSamples)
		for i in range(nSamples):
			data['x0'] += [blob_data[i][0]]
			data['x1'] += [blob_data[i][1]]
			data['weight'] += [1]

		return pd.DataFrame(data)
	if Ndim == 3:
		data = {'x0': [], 'x1': [], 'x2': [], 'weight': []}
		z = np.random.normal(mean,sigma,100)
		centers = []
		for i in range(nBlobs):
			centers.append([sign()*15*rnd.random(),sign()*15*rnd.random()])
		for value in z: # for every z value, a layer is generated.
			blob_data, blob_labels = make_blobs(n_samples=nSamples,centers=np.array(centers))
			for i in range(nSamples):
				data['x0'] += [blob_data[i][0]]
				data['x1'] += [blob_data[i][1]]
				data['x2'] += [value]
				data['weight'] += [1]

		return pd.DataFrame(data)

def testdata(Ndim, noise=False):
	j = 0	
	if Ndim == 2:
		data = {'x0': [], 'x1': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 3:
		data = {'x0': [], 'x1': [], 'x2': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 4:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 5:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'x4': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			data['x4'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 6:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'x4': [], 'x5': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			data['x4'] += list(np.random.normal(j,0.2,1000))
			data['x5'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 7:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'x4': [], 'x5': [], 'x6': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			data['x4'] += list(np.random.normal(j,0.2,1000))
			data['x5'] += list(np.random.normal(j,0.2,1000))
			data['x6'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 8:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'x4': [], 'x5': [], 'x6': [], 'x7': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			data['x4'] += list(np.random.normal(j,0.2,1000))
			data['x5'] += list(np.random.normal(j,0.2,1000))
			data['x6'] += list(np.random.normal(j,0.2,1000))
			data['x7'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 9:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'x4': [], 'x5': [], 'x6': [], 'x7': [], 'x8': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			data['x4'] += list(np.random.normal(j,0.2,1000))
			data['x5'] += list(np.random.normal(j,0.2,1000))
			data['x6'] += list(np.random.normal(j,0.2,1000))
			data['x7'] += list(np.random.normal(j,0.2,1000))
			data['x8'] += list(np.random.normal(j,0.2,1000))
			j += 2
	if Ndim == 10:
		data = {'x0': [], 'x1': [], 'x2': [], 'x3': [], 'x4': [], 'x5': [], 'x6': [], 'x7': [], 'x8': [], 'x9': [], 'weight': []}
		for i in range(3):
			data['x0'] += list(np.random.normal(j,0.2,1000))
			data['x1'] += list(np.random.normal(j,0.2,1000))
			data['x2'] += list(np.random.normal(j,0.2,1000))
			data['x3'] += list(np.random.normal(j,0.2,1000))
			data['x4'] += list(np.random.normal(j,0.2,1000))
			data['x5'] += list(np.random.normal(j,0.2,1000))
			data['x6'] += list(np.random.normal(j,0.2,1000))
			data['x7'] += list(np.random.normal(j,0.2,1000))
			data['x8'] += list(np.random.normal(j,0.2,1000))
			data['x9'] += list(np.random.normal(j,0.2,1000))
			j += 2
	data['weight'] = [1 for i in range(len(data['x0']))]

	df = pd.DataFrame(data)
	return df

class clusterer:
	def __init__(self, dc, rhoc, outlier, pPBin=10): 
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.pPBin = pPBin
	def readData(self, inputData):
		"""
		Reads the data in input and fills the class members containing the coordinates of the points, the energy weight, the number of dimensions and the number of points.

		Parameters:
		inputData (pandas dataframe): The dataframe should contain one column for every coordinate, each one called 'x*', and one column for the weight.
		inputData (string): The string should contain the full path to a csv file containing the data.
		inputData (list or numpy array): The list or numpy array should contain a list of lists for the coordinates and a list for the weight.
		"""

		print('Start loading points')
		
		# numpy array
		if type(inputData) == np.array:
			self.coords = [coord for coord in self.inputData[:-1]]
			self.weight = self.inputData[-1] 
			self.Ndim = len(self.inputData[:-1])
			self.Npoints = len(self.weight)

		# lists
		if type(inputData) == list:
			self.coords = [coord for coord in self.inputData[:-1]]
			self.weight = self.inputData[-1]
			self.Ndim = len(self.inputData[:-1])
			self.Npoints = len(self.weight)

		# path to .csv file or pandas dataframe
		if type(inputData) == str or type(inputData) == pd.DataFrame:
			if type(inputData) == str:
				df = pd.read_csv(inputData)
			if type(inputData) == pd.DataFrame:
				df = inputData

			coordinate_columns = [col for col in df.columns if col[0] == 'x']
			self.Ndim = len(coordinate_columns)
			self.coords = []
			for col in coordinate_columns:
				self.coords.append(list(df[col]))
			self.weight = list(df['weight'])
			self.Npoints = len(self.weight)

		print('Finished loading points')
	def runCLUE(self):
		"""
		Executes the CLUE clustering algorithm.

		Output:
		self.clusterIds (list): Contains the clusterId corresponding to every point.
		self.isSeed (list): For every point the value is 1 if the point is a seed or an outlier and 0 if it isn't.
		self.NClusters (int): Number of clusters reconstructed.
		self.clusterPoints (list): Contains, for every cluster, the list of points associated to id.
		self.pointsPerCluster (list): Contains the number of points associated to every cluster
		"""

		start = time.time_ns()
		clusterIdIsSeed = Algo.mainRun(self.dc,self.rhoc,self.outlier,self.pPBin,self.coords,self.weight,self.Ndim)
		finish = time.time_ns()
		self.clusterIds = clusterIdIsSeed[0]
		self.isSeed = clusterIdIsSeed[1]
		self.NClusters = len(list(set(self.clusterIds))) 

		clusterPoints = [[] for i in range(self.NClusters)]
		for i in range(self.Npoints):
			clusterPoints[self.clusterIds[i]].append(i)

		self.clusterPoints = clusterPoints
		self.pointsPerCluster = [len(clust) for clust in clusterPoints]

		data = {'clusterIds': self.clusterIds, 'isSeed': self.isSeed}
		self.outputDF = pd.DataFrame(data) 

		self.elapsed_time = (finish - start)/(10**6)
		print('CLUE run in ' + str(self.elapsed_time) + ' ms')
		print('Number of clusters found: ', self.NClusters)
	def inputPlotter(self):
		"""
		Plots the the points in input.
		"""

		if self.Ndim == 2:
			plt.scatter(self.coords[0],self.coords[1], s=1)
			plt.show()
		if self.Ndim >= 3:
			fig = plt.figure()
			ax = fig.add_subplot(projection='3d')
			ax.scatter(self.coords[0],self.coords[1],self.coords[2])

			plt.show()
	def clusterPlotter(self):
		"""
		Plots the clusters with a different colour for every cluster. 

		The points assigned to a cluster are prints as points, the seeds as stars and the outliers as little grey crosses. 
		"""
		
		if self.Ndim == 2:
			data = {'x0':self.coords[0], 'x1':self.coords[1], 'clusterIds':self.clusterIds, 'isSeed':self.isSeed}
			df = pd.DataFrame(data)

			df_clindex = df["clusterIds"]
			M = max(df_clindex) 
			dfs = df["isSeed"]

			df_out = df[df.clusterIds == -1] # Outliers
			plt.scatter(df_out.x0, df_out.x1, s=5, marker='x', color='0.4')
			for i in range(0,M+1):
				dfi = df[df.clusterIds == i] # ith cluster
				plt.scatter(dfi.x0, dfi.x1, s=5, marker='.')
			df_seed = df[df.isSeed == 1] # Only Seeds
			plt.scatter(df_seed.x0, df_seed.x1, s=20, color='r', marker='*')
			plt.show()
		if self.Ndim == 3:
			data = {'x0':self.coords[0], 'x1':self.coords[1], 'x2':self.coords[2], 'clusterIds':self.clusterIds, 'isSeed':self.isSeed}
			df = pd.DataFrame(data)

			df_clindex = df["clusterIds"]
			M = max(df_clindex) 
			dfs = df["isSeed"]
			fig = plt.figure()
			ax = fig.add_subplot(projection='3d')

			df_out = df[df.clusterIds == -1]
			ax.scatter(df_out.x0, df_out.x1, df_out.x2, s=15, color = 'grey', marker = 'x')
			for i in range(0,M+1):
				dfi = df[df.clusterIds == i]
				ax.scatter(dfi.x0, dfi.x1, dfi.x2, s=5, marker = '.')

			df_seed = df[df.isSeed == 1] # Only Seeds
			ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s=20, color = 'r', marker = '*')

			plt.show()
	def toCSV(self,outputFolder,fileName):
		"""
		Creates a file containing the coordinates of all the points, their clusterIds and isSeed.	

		Parameters: 
		outputFolder (string): Full path to the desired ouput folder.
		fileName(string): Name of the file, with the '.csv' suffix.
		"""

		outPath = outputFolder + fileName
		data = {}
		for i in range(self.Ndim):
			data['x' + str(i)] = self.coords[i]
		data['clusterIds'] = self.clusterIds
		data['isSeed'] = self.isSeed

		df = pd.DataFrame(data)
		df.to_csv(outPath,index=False)

t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0
for i in range(10):
	c = clusterer(1,40,1.2)
	c.readData(testdata(2))
	c.runCLUE()
	t2 += c.elapsed_time
	d = clusterer(1,40,1.2)
	d.readData(testdata(3))
	d.runCLUE()
	t3 += d.elapsed_time
	e = clusterer(1,40,1.2)
	e.readData(testdata(4))
	e.runCLUE()
	t4 += e.elapsed_time
	f = clusterer(1,40,1.2)
	f.readData(testdata(5))
	f.runCLUE()
	t5 += f.elapsed_time
	g = clusterer(1,40,1.2)
	g.readData(testdata(6))
	g.runCLUE()
	t6 += g.elapsed_time
	h = clusterer(1,40,1.2)
	h.readData(testdata(7))
	h.runCLUE()
	t7 += h.elapsed_time
	i = clusterer(1,40,1.2)
	i.readData(testdata(8))
	i.runCLUE()
	t8 += i.elapsed_time
	j = clusterer(1,40,1.2)
	j.readData(testdata(9))
	j.runCLUE()
	t9 += j.elapsed_time
	k = clusterer(1,40,1.2)
	k.readData(testdata(10))
	k.runCLUE()
	t10 += k.elapsed_time

print(t2/10)
print(t3/10)
print(t4/10)
print(t5/10)
print(t6/10)
print(t7/10)
print(t8/10)
print(t9/10)
print(t10/10)
