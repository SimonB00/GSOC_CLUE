import pandas as pd
import time
import matplotlib.pyplot as plt
import clusteringAlgo 

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

class clusterer:
	def __init__(self, inputFileName, pathOutput, dc, rhoc, outlier, pPBin): 
		self.inputFileName = inputFileName
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.pPBin = pPBin

		# the input name should be like pathToInput/fileName.csv
		inputName = getInputName(self.inputFileName)
		outputFileName = pathOutput + inputName

		for par in [dc,rhoc,outlier,pPBin]:
			outputFileName += '_' + str(par)
		outputFileName += '.csv'
	
		self.outputFileName = outputFileName
	def readData(self):
		print('Start loading points')

		df = pd.read_csv(self.inputFileName, header=None)
		self.Ndim = len(df.columns) - 1 

		self.coords = []
		for j in range(self.Ndim):
			self.coords.append(list(df[j]))
		self.weight = list(df[self.Ndim])

		print('Finished loading points')
	def runCLUE(self):
		clusteringAlgo.mainRun(self.dc,self.rhoc,self.outlier,self.pPBin,self.inputFileName,self.outputFileName,self.Ndim)
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

c = clusterer('../../binding/moon.csv','../../data/output/',1.2,40,0.4,3)
c.readData()
c.inputPlotter()
c.runCLUE()
c.clusterPlotter()
