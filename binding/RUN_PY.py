import pyCLUE
import pandas as pd
import numpy as np
import time

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
        outputFileName += '_' + str(parameters[par])
    outputFileName += ".csv"

    return outputFileName

inputFileName = "../data/input/moon.csv"
pathToOutput = "../data/output/"
parameters = {'dc':5, 'rhoc':10, 'outlier':2, 'ppBin':3}
outputFileName = createOutputName(inputFileName,pathToOutput,parameters)

print('Start loading points')

inputDF = pd.read_csv(inputFileName,header=None)
coords = []
weight = []

for j in range(Ndim):
	coords.append(list(inputDF[j]))
weight = list(inputDF[Ndim])

print('Finished loading points')

print('Start running CLUE')
start = time.time_ns()
clusterer = pyCLUE.clusteringAlgo3(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
clusterer.setPoints(len(weight),coords,weight)
clusterer.makeClusters()
finish = time.time_ns()

elapsed_time = (finish - start)/(10**6)
print('Elapsed time = ' + str(elapsed_time) + ' ms')
print('Finished running CLUE')

clusterer.createOutputFile(outputFileName)
