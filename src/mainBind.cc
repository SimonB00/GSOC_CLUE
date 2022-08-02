#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include "CLUEAlgo.h"
#include <pybind11/pybind11.h>

template <uint8_t N>
void mainRun(std::string inputFileName, std::string outputFileName,
              float dc, float rhoc, float outlierDeltaFactor,
              bool useGPU, int repeats, bool verbose) {

  //////////////////////////////
  // read toy data from csv file
  //////////////////////////////
  std::cout << "Start to load input points" << std::endl;

  //std::vector<float> x;
  //std::vector<float> y;
  std::array<std::vector<float>,N> coordinates;
  std::vector<int> layer;
  std::vector<float> weight;

  // make dummy layers
  for (int l=0; l!=NLAYERS; ++l) {
    // open csv file
    std::ifstream iFile(inputFileName);
    std::string value = "";
    // Iterate through each line and split the content using delimeter
    while (getline(iFile, value, ',')) {
      for(int i = 0; i != N; ++i) {
        coordinates[i].push_back(std::stof(value)) ;
        getline(iFile, value, ','); 
      }
      layer.push_back(std::stoi(value) + l);
      getline(iFile, value); 
      weight.push_back(std::stof(value));
    }
    iFile.close();
  }
  std::cout << "Finished loading input points" << std::endl;

  //////////////////////////////
  // run CLUE algorithm
  //////////////////////////////
  std::cout << "Start to run CLUE algorithm" << std::endl;
  CLUEAlgo<N> clueAlgo(dc, rhoc, outlierDeltaFactor, verbose);
  for (int r = 0; r<repeats; ++r) {
    clueAlgo.setPoints(coordinates[0].size(), coordinates, &layer[0], &weight[0]);
    // measure excution time of makeClusters
    auto start = std::chrono::high_resolution_clock::now();
    clueAlgo.makeClusters();
    auto finish = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = finish - start;
    std::cout << "Elapsed time: " << elapsed.count() *1000 << " ms\n";
  }
  
  // output result to outputFileName. -1 means all points.
  if(verbose)
    clueAlgo.verboseResults(outputFileName, -1);

  std::cout << "Finished running CLUE algorithm" << std::endl;
} // end of testRun()

void RUN(uint8_t N) {
    mainRun<N>();
}

PYBIND11_MODULE(CLUE, m) {
    m.doc() = "pybind11 example plugin";
    m.def("algo", &RUN, "CLUE Algorithm");
}
