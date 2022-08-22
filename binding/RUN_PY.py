import pyCLUE
import pandas as pd
import numpy as np

Ndim = 3

def getInputName(inputFileName):
    size = len(inputFileName)
    name = ''
  
    for i in range(5,size):
        if inputFileName[size-i] == '/':
	        break
        name += inputFileName[size-i]
  
    return name[::-1]

def createOutputName(inputFileName_, pathOutput, parameters):
    # the input name should be like pathToInput/fileName.csv
    inputName = getInputName(inputFileName_)
    outputFileName = pathOutput + inputName

    for par in parameters:
        outputFileName += '_' + str(par)
    outputFileName += ".csv"

    return outputFileName

inputFileName = "../data/input/moon.csv"
pathToOutput = "../data/output/"
parameters = [5,10,2,3]
outputFileName = createOutputName(inputFileName,pathToOutput,parameters)

print('Start loading points')

inputDF = pd.read_csv(inputFileName,header=None)
len_ = len(inputDF.values.tolist())

coords = []
weight = []
for i in range(Ndim):
	coords.append([])

for i in range(len_):
	for j in range(Ndim):
		#coord = 'x' + str(j)
		coords[j].append(inputDF[j][i])
	weight.append(inputDF[len(inputDF.columns)-1][i])

print('Finished loading points')

print('Start running CLUE')
clusterer = pyCLUE.clusteringAlgo3(parameters[0],parameters[1],parameters[2],parameters[3])
clusterer.setPoints(len(weight),coords,weight)
clusterer.makeClusters()
print('Finished running CLUE')

clusterer.createOutputFile(outputFileName)
