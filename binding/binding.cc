#include <pybind11/pybind11.h>
#include "../clustAlgo/clustering.h"
#include "../clustAlgo/main.cc"
#include <pybind11/stl.h> 

PYBIND11_MODULE(clusteringAlgo, m) {
    m.doc() = "Binding for CLUE";

	m.def("mainRun", &mainRun, "mainRun");
}
