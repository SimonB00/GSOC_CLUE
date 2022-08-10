#include <chrono>
#include <iostream>
#include <fstream>
#include <string>

#include "clustering.h"

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
      for(int i = 0; i != Ndim; ++i) {
        coordinates[i].push_back(std::stof(value)) ;
        if(i != Ndim-1) { getline(iFile, value, ','); }   
        if(i == Ndim-1) { getline(iFile, value, '\n'); }
      } 
      weight.push_back(std::stof(value));
    }
    iFile.close();

    std::cout << "Finished loading input points" << '\n';

    // Running the clustering algorithm //
    std::cout << "Run CLUE" << '\n';
    ClusteringAlgo<T,Ndim> algo(dc,rhoc,outlierDeltaFactor,pPBin);
    algo.setPoints(coordinates[0].size(), coordinates, &weight[0]);
    
    auto start_clustering = std::chrono::high_resolution_clock::now();
    algo.makeClusters();
    auto finish_clustering = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
    std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

    std::cout << "Finished running CLUE" << '\n';

    algo.createOutputFile(outputFileName);
}

std::string getInputName(std::string const& inputFileName) {
  int size = inputFileName.size();
  std::string name;
  
  for(int i = 5; i < size; ++i) {
      if(inputFileName[size-i] == '/') { break; }
      name += inputFileName[size-i];
  }
  reverse(name.begin(),name.end());
  
  return name;
}

std::string createOutputName(std::string const& inputFileName_, std::string const& pathOutput, 
                            std::vector<float> const& parameters) {
    // the input name should be like pathToInput/fileName.csv
    std::string inputName = getInputName(inputFileName_);
    std::string outputFileName = pathOutput + inputName;
    for(auto const& par : parameters) {
        outputFileName += '_' + std::to_string(par);
    }
    outputFileName += ".csv";

    return outputFileName;
}

int main(int argc, char *argv[]) {
    float dc=20, rhoc=80, outlierDeltaFactor=2;
    int pPbin = 3;

    if (argc == 5) {
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
    std::cout << inputFileName << '\n';
    std::string pathToOutput = "../data/output/";
    std::vector<float> parameters{dc,rhoc,outlierDeltaFactor};

    std::string outputFileName = createOutputName(inputFileName, pathToOutput, parameters);
    std::cout << outputFileName << '\n',
    //////////////////////////////
    // MARK -- test run
    //////////////////////////////

    mainRun<float,2>(dc, rhoc, outlierDeltaFactor, pPbin,
                    inputFileName, outputFileName);
}