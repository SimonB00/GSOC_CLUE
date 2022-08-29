import pandas as pd
import time
import matplotlib.pyplot as plt

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

def createOutputName(inputFileName_, pathOutput, parameters):	
	# the input name should be like pathToInput/fileName.csv
	inputName = getInputName(inputFileName_)
	outputFileName = pathOutput + inputName

	for par in parameters:
		outputFileName += '_' + str(parameters[par])
	outputFileName += '.csv'
	
	return outputFileName

class clusterer:
	def __init__(self, inputFileName, dc, rhoc, outlier, ppBin): 
		self.inputFileName = inputFileName
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.ppBin = ppBin
	def readData(self):
		print('Start loading points')

		df = pd.read_csv(self.inputFileName, header=None)
		self.Ndim = len(df.columns) - 1 

		self.coords = []
		for j in range(self.Ndim):
			coords.append(list(df[j]))
		self.weight = list(df[self.Ndim])

		print('Finished loading points')
	def chooseClusterer(self):
		if self.Ndim == 2:
			return pyCLUE.clusteringAlgo2(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 3:
			return pyCLUE.clusteringAlgo3(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 4:
			return pyCLUE.clusteringAlgo4(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 5:
			return pyCLUE.clusteringAlgo5(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 6:
			return pyCLUE.clusteringAlgo6(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 7:
			return pyCLUE.clusteringAlgo7(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 8:
			return pyCLUE.clusteringAlgo8(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 9:
			return pyCLUE.clusteringAlgo9(self.dc,self.rhoc,self.outlier,self.ppBin)
		if self.Ndim == 10:
			return pyCLUE.clusteringAlgo10(self.dc,self.rhoc,self.outlier,self.ppBin)
	def runCLUE(self):
		print('Start running CLUE')
		start = time.time_ns()

		clusterer = self.chooseClusterer(self.Ndim)
		clusterer.setPoints(len(self.weight), self.coords, self.weight)
		clusterer.makeClusters()
		finish = time.time_ns()

		elapsed_time = (finish - start)/(10**6)
		print('Elapsed time = ' + str(elapsed_time) + ' ms')
		print('Finished running CLUE')

		clusterer.createOutputFile(self.outputFileName)
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
		df = pd.read_csv(self.inputFileName) 

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
    		dfi = df[df.clusterId == i] #i_th cluster
    		ax.scatter(dfi.x0, dfi.x1, dfi.x2, s = 5, marker = '.')

		df_seed = df[df.isSeed == 1] #Only Seeds
		ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s = 20, color = 'r', marker = '*')

		plt.show()