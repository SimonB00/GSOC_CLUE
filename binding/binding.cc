#include <pybind11/pybind11.h>
#include "../clustAlgo/run.h"
#include <pybind11/stl.h> 

PYBIND11_MODULE(clusteringAlgo, m) {
    m.doc() = "Binding for CLUE";

	m.def("mainRun", &mainRun, "mainRun");
}
