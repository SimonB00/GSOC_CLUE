import pandas as pd
import time

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

def chooseClusterer(Ndim_):
	if Ndim_ == 2:
		return pyCLUE.clusteringAlgo2(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])

class clusterer:
	def __init__(self, inputFileName, dc, rhoc, outlier, ppBin): 
		self.inputFileName = inputFileName
		self.dc = dc
		self.rhoc = rhoc
		self.outlier = outlier
		self.ppBin = ppBin
	def inputPlotter():
		pass
	def clusterPlotter():
		pass
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

		clusterer = chooseClusterer(self.Ndim)
