#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
#include "clustering.h"

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

void run2(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,2> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';

	algo.createOutputFile(outputFileName);
}
			
void run3(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,3> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';

	algo.createOutputFile(outputFileName);
}

void run4(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,4> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';

	algo.createOutputFile(outputFileName);
}

void run5(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates,	std::vector<float> const& weight) {
	ClusteringAlgo<float,5> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';

	algo.createOutputFile(outputFileName);
}

void run6(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,6> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';
}

void run7(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,7> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';
}

void run8(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,8> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';
}

void run9(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,9> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';
}

void run10(float dc, float rhoc, float outlier, int pPBin, std::string outputFileName, 
		std::vector<std::vector<float>> const& coordinates, std::vector<float> const& weight) {
	ClusteringAlgo<float,10> algo(dc,rhoc,outlier,pPBin);
	algo.setPoints(coordinates[0].size(), coordinates, weight);

	auto start_clustering = std::chrono::high_resolution_clock::now();
	algo.makeClusters();
	auto finish_clustering = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_clue = finish_clustering - start_clustering;
	std::cout << "CLUE executed in: " << elapsed_clue.count() *1000 << " ms\n";

	std::cout << "Finished running CLUE" << '\n';
}

void mainRun(float dc, float rhoc, float outlier, int pPBin, 
            std::vector<std::vector<float>> const& coords, std::vector<float> const& weight,
			std::string outputFileName, int Ndim) {

    // Running the clustering algorithm //
    std::cout << "Run CLUE" << '\n';
   	if (Ndim == 2) {
		run2(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 3) {
		run3(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 4) {
		run4(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 5) {
		run5(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 6) {
		run6(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 7) {
		run7(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 8) {
		run8(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 9) {
		run9(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
   	if (Ndim == 10) {
		run10(dc,rhoc,outlier,pPBin,outputFileName,coords,weight);
	} 
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
    std::cout << outputFileName << '\n';
    //////////////////////////////
    // MARK -- test run
    //////////////////////////////

	//    mainRun(dc, rhoc, outlierDeltaFactor, pPbin,
    //               inputFileName, outputFileName, 3);
}
