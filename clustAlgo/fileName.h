#ifndef fileName_h
#define fileName_h

#include <string>
#include <vector>

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
    std::string outputFileName = pathOutput + inputFileName_;
    for(auto const& par : parameters) {
        outputFileName += '_' + std::to_string(par);
    }
    outputFileName += ".csv";

    return outputFileName;
}

#endif