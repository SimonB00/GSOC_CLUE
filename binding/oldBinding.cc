#include <pybind11/pybind11.h>
#include "../clustAlgo/clustering.h"
#include <pybind11/stl.h> 
#include <pybind11/complex.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>

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

    pybind11::class_<ClusteringAlgo<float, 4>>(m, "clusteringAlgo4")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 4>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 4>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 4>::createOutputFile);
		
    pybind11::class_<ClusteringAlgo<float, 5>>(m, "clusteringAlgo5")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 5>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 5>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 5>::createOutputFile);

    pybind11::class_<ClusteringAlgo<float, 6>>(m, "clusteringAlgo6")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 6>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 6>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 6>::createOutputFile);

    pybind11::class_<ClusteringAlgo<float, 7>>(m, "clusteringAlgo7")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 7>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 7>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 7>::createOutputFile);

    pybind11::class_<ClusteringAlgo<float, 8>>(m, "clusteringAlgo8")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 8>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 8>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 8>::createOutputFile);

    pybind11::class_<ClusteringAlgo<float, 9>>(m, "clusteringAlgo9")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 9>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 9>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 9>::createOutputFile);

    pybind11::class_<ClusteringAlgo<float, 10>>(m, "clusteringAlgo10")
        .def(pybind11::init<const float &, const float &, const float &, const int &>())
        .def("setPoints", &ClusteringAlgo<float, 10>::setPoints)
        .def("makeClusters", &ClusteringAlgo<float, 10>::makeClusters)
		.def("createOutputFile", &ClusteringAlgo<float, 10>::createOutputFile);
}
