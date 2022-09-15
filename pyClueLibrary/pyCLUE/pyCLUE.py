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
	Returns a test dataframe containing 2-dimensional or 3-dimensional blobs. 
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
		for value in z:
			blob_data, blob_labels = make_blobs(n_samples=nSamples,centers=np.array(centers))
			for i in range(nSamples):
				data['x0'] += [blob_data[i][0]]
				data['x1'] += [blob_data[i][1]]
				data['x2'] += [value]
				data['weight'] += [1]

		return pd.DataFrame(data)

class clusterer:
	def __init__(self, dc, rhoc, outlier, pPBin=10): 
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.pPBin = pPBin
	def readData(self, inputData):
		"""
		Reads the data in input and fills the class members containing the coordinates of the points, the energy weight, the number of dimensions and the number of points.
		The data can be a numpy array or a native list, containing a list for every coordinate and one for the weight.
		The data can also be a string, containing the full path to a csv file or a pandas dataframe.
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
		start = time.time_ns()
		clusterIdIsSeed = Algo.mainRun(self.dc,self.rhoc,self.outlier,self.pPBin,self.coords,self.weight,self.Ndim)
		finish = time.time_ns()
		self.clusterId = clusterIdIsSeed[0]
		self.isSeed = clusterIdIsSeed[1]
		self.NClusters = len(list(set(self.clusterId))) 

		clusterPoints = []
		for i in range(self.NClusters):
			clusterPoints.append([])

		for i in range(self.Npoints):
			print(self.clusterId[i])
			clusterPoints[self.clusterId[i]].append(i)

		self.clusterPoints = clusterPoints

		elapsed_time = (finish - start)/(10**6)
		print('CLUE run in ' + str(elapsed_time) + ' ms')
		print('Number of clusters found: ', self.NClusters)
	def inputPlotter(self):
		if self.Ndim == 2:
			plt.scatter(self.coords[0],self.coords[1], s=1)
			plt.show()
		if self.Ndim == 3:
			fig = plt.figure()
			ax = fig.add_subplot(projection='3d')
			ax.scatter(self.coords[0],self.coords[1],self.coords[2])

			plt.show()
	def clusterPlotter(self):
		if self.Ndim == 2:
			data = {'x0':self.coords[0], 'x1':self.coords[1], 'clusterId':self.clusterId, 'isSeed':self.isSeed}
			df = pd.DataFrame(data)

			df_clindex = df["clusterId"]
			M = max(df_clindex) 
			dfs = df["isSeed"]

			df_out = df[df.clusterId == -1] # Outliers
			plt.scatter(df_out.x0, df_out.x1, s=5, marker='x', color='0.4')
			for i in range(0,M+1):
				dfi = df[df.clusterId == i] # ith cluster
				plt.scatter(dfi.x0, dfi.x1, s=5, marker='.')
			df_seed = df[df.isSeed == 1] # Only Seeds
			plt.scatter(df_seed.x0, df_seed.x1, s=20, color='r', marker='*')
			plt.show()
		if self.Ndim == 3:
			data = {'x0':self.coords[0], 'x1':self.coords[1], 'x2':self.coords[2], 'clusterId':self.clusterId, 'isSeed':self.isSeed}
			df = pd.DataFrame(data)

			df_clindex = df["clusterId"]
			M = max(df_clindex) 
			dfs = df["isSeed"]
			fig = plt.figure()
			ax = fig.add_subplot(projection='3d')

			df_out = df[df.clusterId == -1]
			ax.scatter(df_out.x0, df_out.x1, df_out.x2, s=15, color = 'grey', marker = 'x')
			for i in range(0,M+1):
				dfi = df[df.clusterId == i]
				ax.scatter(dfi.x0, dfi.x1, dfi.x2, s=5, marker = '.')

			df_seed = df[df.isSeed == 1] # Only Seeds
			ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s=20, color = 'r', marker = '*')

			plt.show()
	def createOutputFile(self,outputFolder,fileName):
		outPath = outputFolder + fileName
		data = {'x0':self.coords[0], 'x1':self.coords[1], 'x2':self.coords[2], 'clusterId':self.clusterId, 'isSeed':self.isSeed}
		df = pd.DataFrame(data)
		df.to_csv(outPath,index=False)

c = clusterer(1.2,40,0.4,3)
c.readData('../../binding/moon.csv')
c.inputPlotter()
c.runCLUE()
c.clusterPlotter()
