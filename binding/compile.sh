#!/usr/bin/bash

g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) binding.cc -o clusteringAlgo$(python3-config --extension-suffix)

cp clusteringAlgo.cpython-310-x86_64-linux-gnu.so ../pyClueLibrary/pyCLUE/
