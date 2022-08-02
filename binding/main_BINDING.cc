#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
//#include "/home/simone/Documents/GSOC/CLUE/clue-master/include/CLUEAlgo.h"
#include "CLUEAlgo.h"
#include <pybind11/pybind11.h>

//template <uint8_t N>
void mainRun(std::string inputFileName, std::string outputFileName,
              float dc, float rhoc, float outlierDeltaFactor,
              bool useGPU, int repeats, bool verbose) {

  //////////////////////////////
  // read toy data from csv file
  //////////////////////////////
  std::cout << "Start to load input points" << std::endl;

  //std::vector<float> x;
  //std::vector<float> y;
  std::vector<float> x;
  std::vector<float> y;
  std::vector<int> layer;
  std::vector<float> weight;

  // make dummy layers
  for (int l=0; l<NLAYERS; l++){
    // open csv file
    std::ifstream iFile(inputFileName);
    std::string value = "";
    // Iterate through each line and split the content using delimeter
    while (getline(iFile, value, ',')) {
      x.push_back(std::stof(value)) ;
      getline(iFile, value, ','); y.push_back(std::stof(value));
      getline(iFile, value, ','); layer.push_back(std::stoi(value) + l);
      getline(iFile, value); weight.push_back(std::stof(value));
    }
    iFile.close();
  }
  std::cout << "Finished loading input points" << std::endl;

  //////////////////////////////
  // run CLUE algorithm
  //////////////////////////////
  std::cout << "Start to run CLUE algorithm" << std::endl;
//  if (useGPU) {
//#ifndef USE_CUPLA
//    CLUEAlgoGPU clueAlgo(dc, rhoc, outlierDeltaFactor,
//			 verbose);
//    for (unsigned r = 0; r<repeats; r++){
//      clueAlgo.setPoints(x.size(), &x[0], &y[0], &layer[0], &weight[0]);
//      // measure excution time of makeClusters
//      auto start = std::chrono::high_resolution_clock::now();
//      clueAlgo.makeClusters();
//      auto finish = std::chrono::high_resolution_clock::now();
//      std::chrono::duration<double> elapsed = finish - start;
//      std::cout << "Iteration " << r;
//      std::cout << " | Elapsed time: " << elapsed.count()*1000 << " ms\n";
//    }
//
//    // output result to outputFileName. -1 means all points.
//    clueAlgo.verboseResults(outputFileName, -1);
//
//#else
//    CLUEAlgoCupla<cupla::Acc> clueAlgo(dc, rhoc, outlierDeltaFactor,
//				       verbose);
//  for (int r = 0; r<repeats; r++){
//    clueAlgo.setPoints(x.size(), &x[0], &y[0], &layer[0], &weight[0]);
//    // measure excution time of makeClusters
//    auto start = std::chrono::high_resolution_clock::now();
//    clueAlgo.makeClusters();
//    auto finish = std::chrono::high_resolution_clock::now();
//    std::chrono::duration<double> elapsed = finish - start;
//    std::cout << "Elapsed time: " << elapsed.count() *1000 << " ms\n";
//  }
//
//  // output result to outputFileName. -1 means all points.
//  if(verbose)
//    clueAlgo.verboseResults(outputFileName, -1);
//#endif


  //} else {
    std::cout << "Using CLUEAlgo: " << std::endl;
    CLUEAlgo clueAlgo(dc, rhoc, outlierDeltaFactor, verbose);
    for (int r = 0; r<repeats; r++){
      clueAlgo.setPoints(x.size(), &x[0], &y[0], &layer[0], &weight[0]);
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
  //}

  std::cout << "Finished running CLUE algorithm" << std::endl;
} // end of testRun()



PYBIND11_MODULE(CLUE, m) {
    m.doc() = "pybind11 example plugin";
    m.def("algo", &mainRun, "CLUE Algorithm");
}
