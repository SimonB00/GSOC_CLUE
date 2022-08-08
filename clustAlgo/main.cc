#include <chrono>
#include <iostream>
#include <fstream>
#include <string>

#include "clustering.h"
#include "fileName.h"

template <typename T, uint8_t Ndim>
void mainRun(float dc, float rhoc, float outlierDeltaFactor, int pPBin, 
            std::string inputFileName, std::string outputFileName) {
    
    // Loading input points //
    std::array<std::vector<T>,Ndim> coordinates;
    std::vector<float> weight;

    std::cout << "Starting to load input points" << '\n';

    std::ifstream iFile(inputFileName);
    std::string value = "";
    // Iterate through each line and split the content using delimeter
    while (getline(iFile, value, ',')) {
      for(int i = 0; i != N; ++i) {
        coordinates[i].push_back(std::stof(value)) ;
        getline(iFile, value, ','); 
      }
      weight.push_back(std::stof(value));
    }
    iFile.close();

    std::cout << "Finished loading input points" << '\n';

    // Running the clustering algorithm //
    std::cout << "Start to run CLUE" << '\n';
    ClusteringAlgo<T,Ndim> algo(dc,rhoc,outlierDeltaFactor,verbose,pPBin);
    algo.setPoints(coordinates[0].size(), coordinates, &weight[0]);
    
    auto start_clustering = std::chrono::high_resolution_clock::now();
    algo.makeClusters();
    auto finish_clustering = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
    std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

    std::cout << "Finished running CLUE" << '\n';
}

int main(int argc, char *argv[]) {
    float dc=20, rhoc=80, outlierDeltaFactor=2;
    int pPbin = 3;

    if (argc == 8) {
      dc = std::stof(argv[2]);
      rhoc = std::stof(argv[3]);
      outlierDeltaFactor = std::stof(argv[4]);
    } else {
      std::cout << "bin/main [fileName] [dc] [rhoc] [outlierDeltaFactor]" << std::endl;
      return 1;
    }

    //////////////////////////////
    // MARK -- set input and output files
    //////////////////////////////

    std::string inputFileName = argv[1];
    std::string pathToOutput;
    std::vector<float> parameters{dc,rhoc,outlierDeltaFactor};

    std::string outputFileName = createOutputName(inputFileName, pathToOutput, parameters);

    //////////////////////////////
    // MARK -- test run
    //////////////////////////////

    mainRun<float,3>(dc, rhoc, outlierDeltaFactor, pPbin,
                    inputFileName, outputFileName);
}

/*
std::string getInputName(std::string const& inputFileName) {
    int pathEnd;
    int suffixStart;
    int size = inputFileName.size();

    for(int i = 0; i < size; ++i) {
        if(inputFileName[size - i] == '/') {
            pathEnd = size - i;
            break;
        }
        if(inputFileName[size - i] == '.') {
            suffixStart = size - i;
        }
    }
    std::string name;
    for(int i = pathEnd+1; i < suffixStart; ++i) {
        name += inputFileName[i];
    }

    return name;
}
*/