import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import clusteringAlgo 
from sklearn.datasets import make_blobs
from varname import nameof

def getInputName(inputFileName):
	inputFileName = inputFileName[::-1]
	name = ''

	start = False
	for char in inputFileName:
		if char == '.':
			start = True
			continue
		if char == '/':
			break
		if start:
			name += char
	
	return name[::-1]
def makeBlobs(nSamples, Ndim):
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
		z = np.random.normal(0,0.5,100)
		for value in z:
			blob_data, blob_labels = make_blobs(n_samples=nSamples)
			for i in range(nSamples):
				data['x0'] += [blob_data[i][0]]
				data['x1'] += [blob_data[i][1]]
				data['x2'] += [value]
				data['weight'] += [1]

		return pd.DataFrame(data)

class clusterer:
	def __init__(self, inputData, pathOutput, dc, rhoc, outlier, pPBin): 
		self.inputData = inputData
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.pPBin = pPBin

		outputFileName = ''
		if type(inputData) == str:
			inputName = getInputName(self.inputData)
			outputFileName = pathOutput + inputName

		if type(inputData) == pd.DataFrame:
			outputFileName = pathOutput

		for par in [dc,rhoc,outlier,pPBin]:
			outputFileName += '_' + str(par)
		outputFileName += '.csv'
	
		self.outputFileName = outputFileName
	def readData(self):
		print('Start loading points')
		
		if type(self.inputData) == str:
			df = pd.read_csv(self.inputData)
			print(df.columns)
			self.Ndim = len([col for col in df.columns if col[0] == 'x'])

		if type(self.inputData) == pd.DataFrame:
			df = self.inputData

		self.coords = []
		coord_cols = [col for col in df.columns if col[0] == 'x']
		for col in coord_cols:
			self.coords.append(list(df[col]))
		self.weight = list(df['weight'])

		print('Finished loading points')
	def runCLUE(self):
		start = time.time_ns()
		clusteringAlgo.mainRun(self.dc,self.rhoc,self.outlier,self.pPBin,self.coords,self.weight,self.outputFileName,self.Ndim)
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
		df = pd.read_csv(self.outputFileName) 

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
			dfi = df[df.clusterId == i]
			ax.scatter(dfi.x0, dfi.x1, dfi.x2, s=5, marker = '.')

		df_seed = df[df.isSeed == 1] # Only Seeds
		ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s=20, color = 'r', marker = '*')

		plt.show()

print(makeBlobs(100,3))
c = clusterer('../../binding/moon.csv','../../data/output/',1.2,40,0.4,3)
c.readData()
c.inputPlotter()
c.runCLUE()
c.clusterPlotter()
