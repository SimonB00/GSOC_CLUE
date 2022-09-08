import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import clusteringAlgo as Algo 
import subprocess as sub
from sklearn.datasets import make_blobs
from varname import nameof

def makeBlobs(nSamples, Ndim, mean=0, dev=0.5):
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
		z = np.random.normal(mean,dev,100)
		for value in z:
			blob_data, blob_labels = make_blobs(n_samples=nSamples)
			for i in range(nSamples):
				data['x0'] += [blob_data[i][0]]
				data['x1'] += [blob_data[i][1]]
				data['x2'] += [value]
				data['weight'] += [1]

		return pd.DataFrame(data)

class clusterer:
	def __init__(self, dc, rhoc, outlier, pPBin): 
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.pPBin = pPBin
	def readData(self, inputData):
		print('Start loading points')
		
		# numpy array
		if type(self.inputData) == np.array:
			self.coords = [coord for coord in self.inputData[:-1]]
			self.weight = self.inputData[-1] 
			self.Ndim = len(self.inputData[:-1])
			self.Npoints = len(self.weight)

		# lists
		if type(self.inputData) == list:
			self.coords = [coord for coord in self.inputData[:-1]]
			self.weight = self.inputData[-1]
			self.Ndim = len(self.inputData[:-1])
			self.Npoints = len(self.weight)

		# path to .csv file or pandas dataframe
		if type(self.inputData) == str or type(self.inputData) == pd.DataFrame:
			if type(self.inputData) == str:
				df = pd.read_csv(self.inputData)
			if type(self.inputData) == pd.DataFrame:
				df = self.inputData

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
		self.clusterId = Algo.mainRun(self.dc,self.rhoc,self.outlier,self.pPBin,self.coords,self.weight,self.Ndim)[0]
		self.isSeed = Algo.mainRun(self.dc,self.rhoc,self.outlier,self.pPBin,self.coords,self.weight,self.Ndim)[1]
		finish = time.time_ns()

		elapsed_time = (finish - start)/(10**6)
		print('CLUE run in ' + str(elapsed_time) + ' ms')
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
			print("min, Max clusterId: ", min(df_clindex), max(df_clindex))
			dfs = df["isSeed"]
			print("Number of seeds:", len([el for el in dfs if el == 1]))

			df_out = df[df.clusterId == -1] # Outliers
			plt.scatter(df_out.x0, df_out.x1, s=5, marker='x', color='0.4')
			for i in range(0,M+1):
				dfi = df[df.clusterId == i] # ith cluster
				plt.scatter(dfi.x0, dfi.x1, s=5, marker='.')
			plt.scatter(df_seed.x0, df_seed.x1, s=20, color='r', marker='*')
			plt.show()
		if self.Ndim == 3:
			data = {'x0':self.coords[0], 'x1':self.coords[1], 'x2':self.coords[2], 'clusterId':self.clusterId, 'isSeed':self.isSeed}
			df = pd.DataFrame(data)

			df_clindex = df["clusterId"]
			M = max(df_clindex) 
			print("min, Max clusterId: ", min(df_clindex), max(df_clindex))
			dfs = df["isSeed"]
			print("Number of seeds:", len([el for el in dfs if el == 1]))
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
		open_file = open(outputFolder + fileName + '.csv', 'w')
		for i in range(self.Npoints):
			open_file.write(str(self.coords[0][i]) + ',' + str(self.coords[0][i])) + ',' +  str(self.coords[0][i])) + ',' + str(self.clusterId[i]) + ',' + str(self.isSeed[i]) + '\n')	
		open_file.close()
			
c = clusterer(1.2,40,0.4,3)
c.readData('../../binding/moon.csv')
c.inputPlotter()
c.runCLUE()
c.clusterPlotter()
