import CLUE
import pandas as pd
import numpy as np

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
      if(inputFileName[size-i] == '/'):
	  	break
      name += inputFileName[size-i]
  }
 
  return name[::-1]

def createOutputName(inputFileName_, pathOutput, parameters):
    # the input name should be like pathToInput/fileName.csv
    inputName = getInputName(inputFileName_)
    outputFileName = pathOutput + inputName

    for par in parameters:
        outputFileName += '_' + str(par)
    outputFileName += ".csv"

    return outputFileName

inputFileName = "data/input/aniso_1000.csv"
outputFileName = "data/output/FIRST_TEST.csv"

Ndim = 3

print('Start loading points')

inputDF = pd.read_csv(inputFileName)
len_ = len(inputDF.values.tolist())

coords = []
weight = []
for i in range(Ndim):
	coords.append([])

for i in range(len_):
	for j in range(Ndim):
		coord = 'x' + str(j)
		coords[j].append(inputDF[coord][i])
	weight.append(inputDF['weight'][i])

print('Finished loading points')

print('Start running CLUE')
clusterer = pyCLUE.ClusteringAlgo(1,2,3,4)
clusterer.makeClusters()
print('Finished running CLUE'))

clusterer.createOutputFile(outputFileName)
