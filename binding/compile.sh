#!/usr/bin/bash

g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) FIRST_BINDING.cc -o pyCLUE$(python3-config --extension-suffix)
