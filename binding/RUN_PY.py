import pyCLUE
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

Ndim = 3

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
    outputFileName += ".csv"

    return outputFileName

inputFileName = "blob_noise.csv"
pathToOutput = "../data/output/"
parameters = {'dc':3, 'rhoc':15, 'outlier':0.8, 'ppBin':3}
outputFileName = createOutputName(inputFileName,pathToOutput,parameters)

print('Start loading points')

inputDF = pd.read_csv(inputFileName,header=None)

coords = []
for j in range(Ndim):
	coords.append(list(inputDF[j]))
weight = list(inputDF[Ndim])

print('Finished loading points')

def chooseClusterer(Ndim_):
	if Ndim_ == 2:
		return pyCLUE.clusteringAlgo2(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 3:
		return pyCLUE.clusteringAlgo3(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 4:
		return pyCLUE.clusteringAlgo4(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 5:
		return pyCLUE.clusteringAlgo5(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 6:
		return pyCLUE.clusteringAlgo6(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 7:
		return pyCLUE.clusteringAlgo7(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 8:
		return pyCLUE.clusteringAlgo8(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 9:
		return pyCLUE.clusteringAlgo9(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
	if Ndim_ == 10:
		return pyCLUE.clusteringAlgo10(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])


print('Start running CLUE')
start = time.time_ns()
#clusterer = pyCLUE.clusteringAlgo3(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'])
clusterer = chooseClusterer(Ndim) 
clusterer.setPoints(len(weight),coords,weight)
clusterer.makeClusters()
finish = time.time_ns()

elapsed_time = (finish - start)/(10**6)
print('Elapsed time = ' + str(elapsed_time) + ' ms')
print('Finished running CLUE')

clusterer.createOutputFile(outputFileName)

if (Ndim == 2):
	outputDF = pd.read_csv(outputFileName)
	df_clindex = outputDF["clusterId"]
	M = max(df_clindex)
	print("min, Max clusterId: ", min(df_clindex), max(df_clindex))

	dfs = outputDF['isSeed']
	print("Number of seeds: ", len([el for el in dfs if el == 1]))

	for i in range(-1,M+1):
		dfi = outputDF[outputDF.clusterId == i] # ith cluster
		plt.scatter(dfi.x0, dfi.x1, s=20, marker = '.')

	df_seed = outputDF[outputDF.isSeed == 1]
	plt.scatter(df_seed.x0, df_seed.x1, s=20, marker = '*')

	plt.show()

if (Ndim == 3):
	outputDF = pd.read_csv(outputFileName)
	df_clindex = outputDF["clusterId"]
	M = max(df_clindex)
	print("min, Max clusterId: ", min(df_clindex), max(df_clindex))

	dfs = outputDF['isSeed']
	print("Number of seeds: ", len([el for el in dfs if el == 1]))

	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	for i in range(-1,M+1):
		dfi = outputDF[outputDF.clusterId == i] # ith cluster
		ax.scatter(dfi.x0, dfi.x1, dfi.x2, s=20, marker = '.')

	df_seed = outputDF[outputDF.isSeed == 1]
	ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s=20, marker = '*')
	ax.set_zlim(-5,5)

	plt.show()
