#include <pybind11/pybind11.h>
#include "../clustAlgo/clustering.h"
//#include "../clustAlgo/main.cc"

PYBIND11_MODULE(CLUE, m) {
    m.doc() = "CLUE First binding attempt";
    pybind11::class_<ClusteringAlgo<float, 2>>(m, "clusteringAlgo")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 2>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 2>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 2>::createOutputFile);
}
