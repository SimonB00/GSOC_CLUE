#
rm *.so

g++ -O3 -std=c++11 -fPIC $(python3 -m pybind11 --includes) binding.cc -o clusteringAlgo$(python3-config --extension-suffix)

cp *.so ../pyClueLibrary/pyCLUE/
