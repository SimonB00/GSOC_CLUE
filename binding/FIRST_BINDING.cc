#include <pybind11/pybind11.h>
#include "../clustAlgo/clustering.h"
#include <pybind11/stl.h> 
#include <pybind11/complex.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
//#include "../clustAlgo/main.cc"

PYBIND11_MODULE(pyCLUE, m) {
    m.doc() = "CLUE First binding attempt";
    pybind11::class_<ClusteringAlgo<float, 2>>(m, "clusteringAlgo2")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 2>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 2>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 2>::createOutputFile);
        
    pybind11::class_<ClusteringAlgo<float, 3>>(m, "clusteringAlgo3")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 3>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 3>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 3>::createOutputFile);
}
