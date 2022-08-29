import pandas as pd

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
	inputName = 

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
