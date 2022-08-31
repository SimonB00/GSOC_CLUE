import clusteringAlgo
import pandas as pd
import numpy as np
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
    outputFileName += ".csv"

    return outputFileName

inputFileName = "moon.csv"
pathToOutput = "../data/output/"
parameters = {'dc':1.2, 'rhoc':40, 'outlier':0.4, 'ppBin':3}
outputFileName = createOutputName(inputFileName,pathToOutput,parameters)

print('Start loading points')

inputDF = pd.read_csv(inputFileName,header=None)
Ndim = len(inputDF.columns) - 1

coords = []
for j in range(Ndim):
	coords.append(list(inputDF[j]))
weight = list(inputDF[Ndim])

print('Finished loading points')

print('Start running CLUE')
start = time.time_ns()
pyCLUE.mainRun(parameters['dc'],parameters['rhoc'],parameters['outlier'],parameters['ppBin'],inputFileName,outputFileName, Ndim)
finish = time.time_ns()

elapsed_time = (finish - start)/(10**6)
print('Elapsed time = ' + str(elapsed_time) + ' ms')
print('Finished running CLUE')

if (Ndim == 2):
	outputDF = pd.read_csv(outputFileName)
	df_clindex = outputDF["clusterId"]
	M = max(df_clindex)
	print("min, Max clusterId: ", min(df_clindex), max(df_clindex))

	dfs = outputDF['isSeed']
	print("Number of seeds: ", len([el for el in dfs if el == 1]))

	df_outl = outputDF[outputDF.clusterId == -1]
	plt.scatter(df_outl.x0, df_outl.x1, s=15, color = 'grey', marker = 'x')
	for i in range(0,M+1):
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

	df_outl = outputDF[outputDF.clusterId == -1]
	ax.scatter(df_outl.x0, df_outl.x1, df_outl.x2, s=15, color = 'grey', marker = 'x')
	for i in range(0,M+1):
		dfi = outputDF[outputDF.clusterId == i] # ith cluster
		ax.scatter(dfi.x0, dfi.x1, dfi.x2, s=20, marker = '.')

	df_seed = outputDF[outputDF.isSeed == 1]
	ax.scatter(df_seed.x0, df_seed.x1, df_seed.x2, s=20, marker = '*')
	ax.set_zlim(-5,5)

	plt.show()
