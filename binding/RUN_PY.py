import pyCLUE
import pandas as pd
import numpy as np

Ndim = 2

#ClusteringAlgo<T,Ndim> algo(dc,rhoc,outlierDeltaFactor,pPBin);
#algo.setPoints(coordinates[0].size(), coordinates, &weight[0]);
    
#auto start_clustering = std::chrono::high_resolution_clock::now();
#algo.makeClusters();
#auto finish_clustering = std::chrono::high_resolution_clock::now();
#std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
#std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

#std::cout << "Finished running CLUE" << '\n';

#algo.createOutputFile(outputFileName);

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

inputFileName = "../data/input/aniso_1000_nl.csv"
pathToOutput = "../data/output/"
parameters = [20,25,2,3]
outputFileName = createOutputName(inputFileName,pathToOutput,parameters)
print(outputFileName)

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

print(coords)
print(weight)
print(len(coords))

print('Finished loading points')

print('Start running CLUE')
clusterer = pyCLUE.clusteringAlgo2(parameters[0],parameters[1],parameters[2],parameters[3])
clusterer.setPoints(Ndim,coords,weight)
clusterer.makeClusters()
print('Finished running CLUE')

clusterer.createOutputFile(outputFileName)
